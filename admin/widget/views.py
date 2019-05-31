import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from .models import Agent

# Create your views here.
def index(request):
	try:
		agents = Agent.objects.filter(is_active=True)

		if (not agents):
			raise ObjectDoesNotExist
		
		metrics = list(agents.first().metric_set.all().values())
		return JsonResponse({"agent": list(agents.values())[0], "metrics": metrics})

	except ObjectDoesNotExist:
		return JsonResponse({"error":"no metrics"})
