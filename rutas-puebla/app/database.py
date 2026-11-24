import os
import redis
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")

redis_client = redis.from_url(
    REDIS_URL,
    decode_responses=True
)


def probar_conexion() -> bool:
    try:
        return bool(redis_client.ping())
    except Exception:
        return False
