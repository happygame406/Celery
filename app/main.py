<<<<<<< HEAD
from fastapi import FastAPI

from app.core.settings import settings
from app.routes.job import router as jobs_router

app = FastAPI(title=settings.APP_TITLE)
=======
from fastapi import FastAPI

from app.core.settings import settings
from app.routes.job import router as jobs_router

app = FastAPI(title=settings.APP_TITLE)
>>>>>>> 6cb3aec290b93be653045ba185c05f0837820868
app.include_router(jobs_router)