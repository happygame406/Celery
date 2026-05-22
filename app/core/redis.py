<<<<<<< HEAD
import redis.asyncio as redis

from app.core.settings import settings

redis_client = redis.from_url(
    url=settings.redis_url,
    decode_responses=True
=======
import redis.asyncio as redis

from app.core.settings import settings

redis_client = redis.from_url(
    url=settings.redis_url,
    decode_responses=True
>>>>>>> 6cb3aec290b93be653045ba185c05f0837820868
)