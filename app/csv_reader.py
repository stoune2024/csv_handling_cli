import csv
from pathlib import Path

from pydantic import ValidationError

from app.exceptions import FileReadError
from app.models import VideoStats


def read_stats(files: list[str]) -> list[VideoStats]:
    stats: list[VideoStats] = []

    for file_name in files:
        path = Path(file_name)

        if not path.exists():
            raise FileReadError(f"File does not exist: {file_name}")

        if not path.is_file():
            raise FileReadError(f"Path is not a file: {file_name}")

        try:
            with path.open(encoding="utf-8", newline="") as file:
                reader = csv.DictReader(file)

                stats.extend(VideoStats(**row) for row in reader)

        except ValidationError as exc:
            raise FileReadError(f"Invalid CSV data in '{file_name}'") from exc

        except OSError as exc:
            raise FileReadError(f"Failed to read '{file_name}'") from exc

    return stats
