from django.conf.urls import url
from dashboard.views import DashboardView, upload_file, delete_file, new_folder

urlpatterns = [
	url(r'^$', DashboardView.as_view(), name="dashboard_home"),
	url(r'^folder_contents/$', DashboardView.as_view(), name="folder_contents"),
	url(r'^upload_file/$', upload_file, name="upload_file"),
	url(r'^delete_file/$', delete_file, name="delete_file"),
	url(r'^new_folder/$', new_folder, name="new_folder"),
]