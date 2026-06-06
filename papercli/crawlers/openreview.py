from collections.abc import Iterator

import openreview
import openreview.api

from papercli.base import Crawler, register
from papercli.models import Paper

VENUE_IDS = {
    ("NeurIPS", 2025): "NeurIPS.cc/2025/Conference",
    ("NeurIPS", 2024): "NeurIPS.cc/2024/Conference",
    ("NeurIPS", 2023): "NeurIPS.cc/2023/Conference",
    ("ICML", 2025): "ICML.cc/2025/Conference",
    ("ICML", 2024): "ICML.cc/2024/Conference",
    ("ICML", 2023): "ICML.cc/2023/Conference",
    ("ICLR", 2026): "ICLR.cc/2026/Conference",
    ("ICLR", 2025): "ICLR.cc/2025/Conference",
    ("ICLR", 2024): "ICLR.cc/2024/Conference",
    ("ICLR", 2023): ("ICLR.cc/2023/Conference", 1),
}


def _value(content: dict, key: str):
    field = content.get(key)
    return field.get("value") if isinstance(field, dict) else field


@register
class OpenReviewCrawler(Crawler):
    name = "openreview"
    venues = ["NeurIPS", "ICML", "ICLR"]

    @property
    def supported_venue_years(self) -> list[tuple[str, int]]:
        return list(VENUE_IDS.keys())

    def __init__(self):
        self.client_v2 = openreview.api.OpenReviewClient(
            baseurl="https://api2.openreview.net"
        )
        self._client_v1 = None

    @property
    def client_v1(self):
        if self._client_v1 is None:
            self._client_v1 = openreview.Client(baseurl="https://api.openreview.net")
        return self._client_v1

    def fetch(self, venue: str, year: int) -> Iterator[Paper]:
        mapping = VENUE_IDS.get((venue, year))
        if mapping is None:
            raise KeyError(f"Unknown venueid for {venue} {year}; add it to VENUE_IDS")

        if isinstance(mapping, tuple):
            venueid, version = mapping
        else:
            venueid, version = mapping, 2

        client = self.client_v1 if version == 1 else self.client_v2

        for note in client.get_all_notes(content={"venueid": venueid}):
            content = note.content
            pdf = _value(content, "pdf") or ""
            pdf_url = "https://openreview.net" + pdf if pdf.startswith("/") else pdf
            yield Paper(
                title=_value(content, "title") or "",
                authors=list(_value(content, "authors") or []),
                abstract=_value(content, "abstract"),
                venue=venue,
                year=year,
                track=_value(content, "venue"),
                source="openreview",
                pdf_url=pdf_url,
                forum_url=f"https://openreview.net/forum?id={note.forum}",
            )
