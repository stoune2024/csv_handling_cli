
from app.cli import main


def test_cli_success(tmp_path, capsys):
    file = tmp_path / "stats.csv"

    file.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\nVideo,20,30,100,10,5\n",
        encoding="utf-8",
    )

    exit_code = main(
        [
            "--files",
            str(file),
            "--report",
            "clickbait",
        ]
    )

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Video" in captured.out


def test_cli_invalid_report(tmp_path, capsys):
    file = tmp_path / "stats.csv"

    file.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\nVideo,20,30,100,10,5\n",
        encoding="utf-8",
    )

    exit_code = main(
        [
            "--files",
            str(file),
            "--report",
            "unknown",
        ]
    )

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Unknown report" in captured.err
