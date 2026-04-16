from pydantic import BaseModel, ConfigDict, Field


class VideoStats(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
        str_strip_whitespace=True,
    )

    title: str = Field(min_length=1)
    ctr: float = Field(ge=0)
    retention_rate: float = Field(ge=0, le=100)
    views: int = Field(ge=0)
    likes: int = Field(ge=0)
    avg_watch_time: float = Field(ge=0)
