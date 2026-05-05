
import time, hashlib, os
try:
    import redis
    REDIS_URL = os.getenv("REDIS_URL")
    _redis = redis.from_url(REDIS_URL) if REDIS_URL else None
except Exception:
    _redis = None

_local = {}
TTL = int(os.getenv("CACHE_TTL_SECONDS", "900"))

def _key(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()

def get(prompt: str):
    k = _key(prompt)
    if _redis:
        val = _redis.get(k)
        return val.decode() if val else None
    item = _local.get(k)
    if not item:
        return None
    val, exp = item
    if time.time() > exp:
        _local.pop(k, None)
        return None
    return val

def set(prompt: str, value: str):
    k = _key(prompt)
    if _redis:
        _redis.setex(k, TTL, value)
        return
    _local[k] = (value, time.time() + TTL)
