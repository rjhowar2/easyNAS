from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings

import requests
import urllib

class DashboardView(TemplateView):

    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['folder_contents'] = get_files_from_server()
        return context

def get_files_from_server(path=""):
	base_dir_url = settings.FILE_SERVER_URLS['BASE_DIR']

	try:
		base_dir = requests.get(base_dir_url).json()['base_directory']
	except Exception, e:
		base_dir = ''

	args = {"path": base_dir}
	url = "%s?%s" % (settings.FILE_SERVER_URLS['CONTENTS'], urllib.urlencode(args))

	response = requests.get(url)

	return response.json()

