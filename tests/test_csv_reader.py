import pytest

from app.csv_reader import read_stats
from app.exceptions import FileReadError


def test_missing_file():
    with pytest.raises(FileReadError):
        read_stats(["missing.csv"])


def test_directory_instead_of_file(tmp_path):
    with pytest.raises(FileReadError):
        read_stats([str(tmp_path)])


@pytest.mark.parametrize(
    "bad_row",
    [
        "Video,-1,30,100,10,5",
        "Video,20,101,100,10,5",
        "Video,20,30,-5,10,5",
    ],
)
def test_invalid_csv_data(tmp_path, bad_row):
    file = tmp_path / "bad.csv"

    file.write_text(
        f"title,ctr,retention_rate,views,likes,avg_watch_time\n{bad_row}\n",
        encoding="utf-8",
    )

    with pytest.raises(FileReadError):
        read_stats([str(file)])
