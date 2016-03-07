from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings

import requests
import urllib
import json

class DashboardView(TemplateView):

    template_name  = "dashboard/dashboard.html"
    def get_context_data(self, **kwargs):
    	folder = self.request.GET.get('path','')

        context = super(TemplateView, self).get_context_data(**kwargs)
        folder_contents = get_files_from_server(folder)
        folders = _get_folders(folder_contents["files"]["parent"])
        context['folder_contents'] = get_files_from_server(folder)
        context['folders'] = folders
        context['api_urls'] = settings.FILE_SERVER_URLS
        
        return context

def get_files_from_server(folder):
	args = {"path": folder}
	url = "%s?%s" % (settings.FILE_SERVER_URLS['CONTENTS'], urllib.urlencode(args))

	response = requests.get(url)
	return response.json()

def _get_folders(full_path):
    folders = full_path.lstrip("/").split("/") if full_path else []
    paths = []

    p = ""
    for folder in folders:
        p = "%s/%s" % (p, folder)
        paths.append((p,folder))

    return paths


