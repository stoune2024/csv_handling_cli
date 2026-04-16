from app.models import VideoStats
from app.reports.base import BaseReport
from app.reports.registry import register_report


@register_report
class ClickbaitReport(BaseReport):
    name = "clickbait"

    def build(self, stats: list[VideoStats]) -> list[dict]:
        rows = [
            {
                "title": item.title,
                "ctr": item.ctr,
                "retention_rate": item.retention_rate,
            }
            for item in stats
            if item.ctr > 15 and item.retention_rate < 40
        ]

        return sorted(rows, key=lambda row: row["ctr"], reverse=True)
