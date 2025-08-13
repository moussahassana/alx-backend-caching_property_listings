from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property
from .utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    queryset = get_all_properties()
    data = list(queryset.values())
    return JsonResponse({"data": data})