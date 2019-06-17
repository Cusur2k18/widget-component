from django.conf import settings
from django.contrib import messages
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.shortcuts import render, redirect
from django.core.cache import cache
from .models import Agent

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
COLORS = {
		3: ['green', 'yellow', 'red'],
		5: ['blue', 'green', 'yellow', 'orange', 'red'],
		6: ['green', 'yellow', 'orange', 'red', 'purple', 'redbrown']
}

@cache_page(CACHE_TTL)
def widget(request):
	agents = Agent.objects.prefetch_related('metric_set', 'widget').filter(is_active=True)
	agent = agents.first()

	if (agent is not None):
		return render(request, 'widget/agent.html', { "agent": agent, "colors": COLORS, "total": range(1, agent.widget.total_level + 1) })
	
	return render(request, 'partials/404.html', {})

def preview(request, id):
	# import pdb; pdb.set_trace()
	agent = Agent.objects.prefetch_related('metric_set', 'widget').get(pk=id)
	return render(request, 'widget/agent.html', { "agent": agent, "colors": COLORS, "total": range(1, agent.widget.total_level + 1), "preview": True })



def clear_cache(request):
	# import pdb; pdb.set_trace()
	cache.clear()
	messages.add_message(request, messages.INFO, 'caché borrado exitosamente!.')
	return redirect(request.POST['uri'])
