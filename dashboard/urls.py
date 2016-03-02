from django.conf.urls import url
from dashboard.views import DashboardView

urlpatterns = [
	url(r'^$', DashboardView.as_view(), name="dashboard_home"),
	url(r'^folder_contents/$', DashboardView.as_view(), name="folder_contents"),
]