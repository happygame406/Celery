from datetime import datetime, UTC
from enum import StrEnum
from uuid import UUID, uuid4
from typing import Optional

from sqlalchemy import DateTime
from sqlmodel import Field, SQLModel


class JobStatus(StrEnum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    DONE = "DONE"
    FAILED = "FAILED"


class JobType(StrEnum):
    HTTP_CHECK = "HTTP_CHECK"
    WORD_STATS = "WORD_STATS"
    WORD_STATS_COMPARE = "WORD_STATS_COMPARE"


class QueueName(StrEnum):
    DEFAULT = "default"
    PRIORITY = "priority"


class JobCreate(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    job_type: JobType
    payload: dict | None = None


class JobOut(SQLModel):
    id: UUID
    title: str
    job_type: JobType
    status: JobStatus
    created_at: datetime
    finished_at: Optional[datetime] = None
    error: Optional[str] = None
    payload: Optional[dict] = None
    result: Optional[dict] = None


class JobsSummaryOut(SQLModel):
    pending: int
    processing: int
    done: int
    failed: int


class JobDB(SQLModel, table=True, extend_existing=True):
    __tablename__ = "jobs"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str = Field(min_length=1, max_length=200)
    job_type: str | None = Field(default=None, max_length=100)
    status: JobStatus = Field(default=JobStatus.PENDING)
    
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_type=DateTime(timezone=True)
    )
    
    finished_at: Optional[datetime] = Field(
        default=None,
        sa_type=DateTime(timezone=True)
    )
    
    error: Optional[str] = Field(default=None, max_length=2000)
    payload: Optional[str] = Field(default=None, max_length=5000)
    result: Optional[str] = Field(default=None, max_length=5000)