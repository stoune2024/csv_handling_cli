import pytest

from app.models import VideoStats


@pytest.fixture
def sample_stats():
    return [
        VideoStats(
            title="A",
            ctr=18,
            retention_rate=35,
            views=100,
            likes=10,
            avg_watch_time=5,
        ),
        VideoStats(
            title="B",
            ctr=25,
            retention_rate=20,
            views=100,
            likes=10,
            avg_watch_time=5,
        ),
        VideoStats(
            title="C",
            ctr=10,
            retention_rate=50,
            views=100,
            likes=10,
            avg_watch_time=5,
        ),
    ]
