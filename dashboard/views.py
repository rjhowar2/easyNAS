from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings

import requests
import urllib

class DashboardView(TemplateView):

    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['data'] = get_files_from_server()
        return context

def get_files_from_server(path=None):
	if path == None:
		path = "/"

	args = {"path": path}
	url = "%s?%s" % (settings.FILE_SERVER_URL, urllib.urlencode(args))

	response = requests.get(url)

	return response.json()

