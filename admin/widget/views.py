import json
from django.http import JsonResponse
from .models import Agent

# Create your views here.
def index(request):
    data = list(Agent.objects.values())
    return JsonResponse(data, safe=False)
