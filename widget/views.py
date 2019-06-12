import json
from django.http import JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from .models import Agent


def widget(request):
	agents = Agent.objects.prefetch_related('metric_set', 'widget').filter(is_active=True)
	agent = agents.first()
	colors = {
		3: ['green', 'yellow', 'red'],
		5: ['blue', 'green', 'yellow', 'orange', 'red'],
		6: ['green', 'yellow', 'orange', 'red', 'purple', 'redbrown']
	}
	# import pdb; pdb.set_trace()
	if (agent is not None):
		return render(request, 'widget/agent.html', { "agent": agent, "colors": colors, "total": range(1, agent.widget.total_level + 1) })
	
	return render(request, 'partials/404.html', {})
