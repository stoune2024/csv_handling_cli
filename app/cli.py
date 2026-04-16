import argparse
import sys
from typing import Sequence

from app.csv_reader import read_stats
from app.exceptions import AppError
from app.reports import __all__  # noqa: F401
from app.reports.registry import get_report
from app.table import render_table


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="CSV files with YouTube statistics",
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Report name",
    )

    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)

    try:
        stats = read_stats(args.files)
        report = get_report(args.report)

        rows = report.build(stats)

        print(render_table(rows))
        return 0

    except AppError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
