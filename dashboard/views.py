from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.core.servers.basehttp import FileWrapper
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

    content = r.json()

    return JsonResponse(content)

def download_file(request):
    download_url = settings.FILE_SERVER_URLS["DOWNLOADS"]

    folder = request.POST.get("folder")
    filename = request.POST.getlist("filename")

    r = requests.post(download_url, data={'folder': folder, 'filename': filename}, stream=True)
    if r.status_code == 200:
        response = HttpResponse(FileWrapper(r.raw), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=myfile.zip'
    else:
        response = HttpResponse("Sorry an error occured processing your request")
        response.status_code = 400
    
    return response

def delete_file(request):
    delete_url = settings.FILE_SERVER_URLS["DELETES"]

    folder = request.POST.get("folder")
    filename = request.POST.getlist("filename")

    r = requests.post(delete_url, data={'folder': folder, 'filename': filename})
    content = r.json()

    return JsonResponse(content)

def new_folder(request):
    create_url = settings.FILE_SERVER_URLS["CREATE"]

    folder = request.POST.get("folder")
    name = request.POST.get("name")

    r = requests.post(create_url, data={'folder': folder, 'name': name})
    content = r.json()

    return JsonResponse(content)

def update_file(request):
    update_url = settings.FILE_SERVER_URLS['FILES']

    source = request.POST.get("source")
    dest = request.POST.get("destination")

    r = requests.put(update_url, data={'source': source, 'destination': dest})
    content = r.json()

    return JsonResponse(content)

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


