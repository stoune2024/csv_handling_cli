import pytest

from app.exceptions import UnknownReportError
from app.reports.clickbait import ClickbaitReport
from app.reports.registry import get_report


def test_get_existing_report():
    report = get_report("clickbait")

    assert isinstance(report, ClickbaitReport)


def test_unknown_report():
    with pytest.raises(UnknownReportError):
        get_report("invalid")
