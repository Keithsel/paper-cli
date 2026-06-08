import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

from papercli.base import _venue_year_key
from papercli.db import Store
from papercli.models import Paper


def test_venue_year_key():
    assert _venue_year_key(("AAAI", 2024)) == ("aaai", "aaai", 2024)
    assert _venue_year_key(("ACL", 2023)) == ("acl", "acl", 2023)
    assert _venue_year_key(("CVPR", 2025)) == ("cvf", "cvpr", 2025)

    items = [("CVPR", 2025), ("ACL", 2023), ("AAAI", 2024)]
    sorted_items = sorted(items, key=_venue_year_key)
    assert sorted_items == [("AAAI", 2024), ("ACL", 2023), ("CVPR", 2025)]


@patch("huggingface_hub.HfApi")
def test_sync_hf_logic(mock_hf_api_class):
    mock_api = MagicMock()
    mock_hf_api_class.return_value = mock_api

    mock_info = MagicMock()
    mock_info.sha = "dummy-sha-123"
    mock_api.repo_info.return_value = mock_info

    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "papers.db"
        store = Store(db_path)

        paper1 = Paper(
            title="A dummy paper",
            authors=["Alice"],
            venue="ACL",
            year=2023,
            source="acl",
            pdf_url="http://example.com/paper.pdf",
        )
        store.upsert([paper1])

        expected_pdf_path = f"pdfs/acl/2023/{paper1.id}.pdf"
        mock_api.list_repo_files.return_value = [expected_pdf_path]

        with (
            patch("papercli.cli.Store", return_value=store),
            patch("papercli.cli.DEFAULT_DB", db_path),
        ):
            from papercli.cli import _sync_hf_logic

            conn = store.conn
            row = conn.execute(
                "SELECT pdf_path FROM papers WHERE id=?", (paper1.id,)
            ).fetchone()
            assert not row["pdf_path"]

            _sync_hf_logic()

            row = conn.execute(
                "SELECT pdf_path FROM papers WHERE id=?", (paper1.id,)
            ).fetchone()
            assert row["pdf_path"] == f"hf://{expected_pdf_path}"


def test_upsert_does_not_overwrite_pdf_path():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "papers.db"
        store = Store(db_path)

        paper1 = Paper(
            title="A dummy paper",
            authors=["Alice"],
            venue="ACL",
            year=2023,
            source="acl",
            pdf_url="http://example.com/paper.pdf",
        )
        store.upsert([paper1])

        store.set_pdf_path(paper1.id, "/path/to/local.pdf")

        store.upsert([paper1])

        conn = store.conn
        row = conn.execute(
            "SELECT pdf_path FROM papers WHERE id=?", (paper1.id,)
        ).fetchone()
        assert row["pdf_path"] == "/path/to/local.pdf"
