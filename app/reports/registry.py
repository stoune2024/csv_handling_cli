from typing import Type

from app.exceptions import UnknownReportError
from app.reports.base import BaseReport


REPORTS: dict[str, Type[BaseReport]] = {}


def register_report(report_cls: Type[BaseReport]) -> Type[BaseReport]:
    REPORTS[report_cls.name] = report_cls
    return report_cls


def get_report(name: str) -> BaseReport:
    report_cls = REPORTS.get(name)

    if report_cls is None:
        available = ", ".join(sorted(REPORTS))
        raise UnknownReportError(
            f"Unknown report '{name}'. Available reports: {available}"
        )

    return report_cls()
