from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.conf import settings

import requests
import urllib
import json

class DashboardView(TemplateView):

    def get_template_names(self):
        if self.request.is_ajax():
            return ["dashboard/folder_contents.html"]
        else:
            return ["dashboard/dashboard.html"]

    def get_context_data(self, **kwargs):
    	folder = self.request.GET.get('path','')
        folder_contents = get_files_from_server(folder)
        parent_folder = folder_contents["files"]["parent"]
        folders = _get_folders(parent_folder)

        context = super(TemplateView, self).get_context_data(**kwargs)
        context['folder_contents'] = get_files_from_server(folder)
        context['folders'] = folders
        context['parent'] = parent_folder
        
        return context

def upload_file(request):
    folder = request.POST.get("folder")
    files = {'file': request.FILES['file']}
    upload_url = settings.FILE_SERVER_URLS["FILES"]

    r = requests.post(upload_url, files=files, data={'folder': folder})

    response = r.json()

    return JsonResponse(response)

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


