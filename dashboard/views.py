from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings

import requests

class DashboardView(TemplateView):

    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['files'] = get_files_from_server()
        return context

def get_files_from_server(root=None):
	if root == None:
		root = "/"

	url = settings.FILE_SERVER_URL
	data = {"root": root}
	
	response = requests.post(url, json=data)

	return response.json()['files']

