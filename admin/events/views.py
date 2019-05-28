import json
from django.http import JsonResponse
from .models import Event

# Create your views here.
def index(request):
    data = list(Event.objects.values())
    return JsonResponse(data, safe=False)
