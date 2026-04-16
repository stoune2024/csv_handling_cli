from abc import ABC, abstractmethod

from app.models import VideoStats


class BaseReport(ABC):
    name: str

    @abstractmethod
    def build(self, stats: list[VideoStats]) -> list[dict]:
        raise NotImplementedError
