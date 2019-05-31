import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from .models import Agent

# Create your views here.
def index(request):
	try:
		agent = Agent.objects.filter(is_active=True).first()
		metrics = list(agent.metric_set.all().values())
		return JsonResponse({"agent": model_to_dict(agent), "metrics": metrics})
	except (ObjectDoesNotExist, IndexError,):
		return JsonResponse({"error":"no metrics"})
