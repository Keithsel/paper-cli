from pathlib import Path

from papercli.crawlers.cvf import CVFCrawler
from papercli.crawlers.jmlr import JMLRCrawler
from papercli.crawlers.ijcai import IJCAICrawler
from papercli.crawlers.ecva import ECVACrawler
from papercli.crawlers.isca import ISCACrawler
from papercli.crawlers.aaai import AAAICrawler

FIXTURES = Path(__file__).parent / "fixtures"


def _read(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


def test_cvf_parse():
    papers = list(CVFCrawler()._parse(_read("cvf.html"), "WACV", 2024))
    assert len(papers) == 2

    foo = papers[0]
    assert foo.title == "Foo: A Method"
    assert foo.authors == ["Alice Smith", "Bob Jones"]
    assert (
        foo.pdf_url
        == "https://openaccess.thecvf.com/content/WACV2024/papers/Foo_paper.pdf"
    )
    assert foo.venue == "WACV" and foo.year == 2024 and foo.source == "cvf"

    bar = papers[1]
    assert bar.authors == ["Carol White"]
    assert bar.pdf_url.endswith("Bar_paper.pdf")


def test_jmlr_parse():
    papers = list(JMLRCrawler()._parse(_read("jmlr.html"), "JMLR", 2024))
    assert len(papers) == 2
    assert papers[0].title == "On Truthing Issues"
    assert papers[0].authors == ["Jonathan K. Su"]
    assert papers[0].pdf_url == "https://jmlr.org/papers/volume25/19-301/19-301.pdf"
    assert papers[1].authors == ["Yuze Han", "Guangzeng Xie", "Zhihua Zhang"]


def test_ijcai_parse():
    papers = list(IJCAICrawler()._parse(_read("ijcai.html"), "IJCAI", 2024))
    assert len(papers) == 2
    p0 = papers[0]
    assert p0.title == "Certified Policy Verification"
    assert p0.authors == ["S. Akshay", "Krishnendu Chatterjee"]
    assert p0.pdf_url == "https://www.ijcai.org/proceedings/2024/0001.pdf"
    assert p0.forum_url == "https://www.ijcai.org/proceedings/2024/1"


def test_ecva_parse():
    papers = list(
        ECVACrawler()._parse(_read("ecva.html"), "ECCV", 2024, "ECCV 2024 Papers")
    )
    assert len(papers) == 1
    p0 = papers[0]
    assert (
        p0.title
        == "Is Retain Set All You Need in Machine Unlearning? Restoring Performance of Unlearned Models with Out-Of-Distribution Images"
    )
    assert p0.authors == ["Jacopo Bonato", "Marco Cotogni", "Luigi Sabetta"]
    assert (
        p0.pdf_url
        == "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00004.pdf"
    )
    assert (
        p0.forum_url
        == "https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4_ECCV_2024_paper.php"
    )


def test_isca_parse():
    papers = list(
        ISCACrawler()._parse(
            _read("isca.html"),
            "Interspeech",
            2024,
            "https://www.isca-archive.org/interspeech_2024/",
        )
    )
    assert len(papers) == 2
    p0 = papers[0]
    assert p0.title == "Towards Responsible Speech Processing"
    assert p0.authors == ["Isabel Trancoso"]
    assert (
        p0.pdf_url
        == "https://www.isca-archive.org/interspeech_2024/trancoso24_interspeech.pdf"
    )
    assert (
        p0.forum_url
        == "https://www.isca-archive.org/interspeech_2024/trancoso24_interspeech.html"
    )

    p1 = papers[1]
    assert (
        p1.title
        == "The influence of L2 accent strength and different error types on personality trait ratings"
    )
    assert p1.authors == [
        "Sarah Wesolek",
        "Piotr Gulgowski",
        "Joanna Blaszczak",
        "Marzena Zygis",
    ]
    assert (
        p1.pdf_url
        == "https://www.isca-archive.org/interspeech_2024/wesolek24_interspeech.pdf"
    )
    assert (
        p1.forum_url
        == "https://www.isca-archive.org/interspeech_2024/wesolek24_interspeech.html"
    )


def test_aaai_parse():
    papers = list(AAAICrawler()._parse_issue(_read("aaai.html"), 2026))
    assert len(papers) == 2

    p0 = papers[0]
    assert (
        p0.title
        == "Resource Efficient Sleep Staging via Multi-Level Masking and Prompt Learning"
    )
    assert p0.authors == [
        "Lejun Ai",
        "Yulong Li",
        "Haodong Yi",
        "Jixuan Xie",
        "Yue Wang",
        "Jia Liu",
        "Min Chen",
        "Rui Wang",
    ]
    assert p0.pdf_url == "https://ojs.aaai.org/index.php/AAAI/article/view/36958/40920"
    assert p0.forum_url == "https://ojs.aaai.org/index.php/AAAI/article/view/36958"
    assert p0.venue == "AAAI"
    assert p0.year == 2026
    assert p0.source == "aaai"

    p1 = papers[1]
    assert (
        p1.title == "AutoMalDesc: Large-Scale Script Analysis for Cyber Threat Research"
    )
    assert p1.authors == [
        "Alexandru-Mihai Apostu",
        "Andrei Preda",
        "Alexandra Daniela Damir",
    ]
    assert p1.pdf_url == "https://ojs.aaai.org/index.php/AAAI/article/view/36959/40921"
    assert p1.forum_url == "https://ojs.aaai.org/index.php/AAAI/article/view/36959"
