from app.reports.clickbait import ClickbaitReport


def test_clickbait_report_filters_and_sorts(sample_stats):
    report = ClickbaitReport()

    result = report.build(sample_stats)

    assert result == [
        {
            "title": "B",
            "ctr": 25,
            "retention_rate": 20,
        },
        {
            "title": "A",
            "ctr": 18,
            "retention_rate": 35,
        },
    ]
