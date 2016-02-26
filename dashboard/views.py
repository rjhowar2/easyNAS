from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings

import requests
import urllib
import json

class DashboardView(TemplateView):

    #template_name = "dashboard/dashboard.html"

    def get_template_names(self):
    	if self.request.is_ajax():
        	return ["dashboard/folder_contents.html"]
        else:
        	return ["dashboard/dashboard.html"]

    def get_context_data(self, **kwargs):
    	folder = self.request.GET.get('path','')

        context = super(TemplateView, self).get_context_data(**kwargs)
        context['folder_contents'] = get_files_from_server(folder)
        context['api_urls'] = settings.FILE_SERVER_URLS
        
        return context

def get_files_from_server(folder):
	args = {"path": folder}
	url = "%s?%s" % (settings.FILE_SERVER_URLS['CONTENTS'], urllib.urlencode(args))

	print "url - %s" % url
	response = requests.get(url)
	return response.json()

