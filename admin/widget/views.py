import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Agent

# Create your views here.
def index(request):
  try:
    data = list(Agent.objects.filter(is_active=True).values())[0]
    return JsonResponse(data, safe=False)
  except (ObjectDoesNotExist, IndexError,):
    return JsonResponse({"error": 'no metrics'}, safe=False)
