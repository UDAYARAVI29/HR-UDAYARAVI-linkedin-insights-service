import redis
import os
import json

class Cache:
    def __init__(self):
        self.redis_client = redis.Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            db=0,
            decode_responses=True
        )

    def set_cache(self, key: str, value: dict, expiry: int = 3600):
        """Store data in Redis cache with expiration time (default: 1 hour)"""
        self.redis_client.setex(key, expiry, json.dumps(value))

    def get_cache(self, key: str):
        """Retrieve cached data from Redis"""
        cached_data = self.redis_client.get(key)
        return json.loads(cached_data) if cached_data else None

    def delete_cache(self, key: str):
        """Remove specific cache key"""
        self.redis_client.delete(key)

# Example usage:
# cache = Cache()
# cache.set_cache("test", {"data": "example"}, 300)
# print(cache.get_cache("test"))
