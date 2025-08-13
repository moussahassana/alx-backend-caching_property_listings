import logging
from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection
def get_all_properties():
    """
    Return the Property queryset, cached in Redis for 1 hour.
    Cache key: 'all_properties'
    """
    queryset = cache.get('all_properties')
    if queryset is None:
        queryset = Property.objects.all()
        cache.set('all_properties', queryset, 3600)  # 3600 seconds = 1 hour
    return queryset

def get_redis_cache_metrics():
    """
    Retrieve Redis cache metrics using django_redis, including keyspace_hits,
    keyspace_misses, and a computed hit_ratio (hits / (hits + misses)).
    """
    conn = get_redis_connection("default")
    info = conn.info()  # pulls Redis INFO

    hits = int(info.get("keyspace_hits", 0))
    misses = int(info.get("keyspace_misses", 0))
    total = hits + misses
    hit_ratio = (hits / total) if total > 0 else 0.0

    metrics = {
        "keyspace_hits": hits,
        "keyspace_misses": misses,
        "hit_ratio": hit_ratio,
    }

    logger.info("Redis cache metrics: %s", metrics)
    return metrics