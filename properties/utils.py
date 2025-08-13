from django.core.cache import cache
from .models import Property

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
