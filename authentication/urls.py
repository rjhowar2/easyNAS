from django.conf.urls import url
from django.views.generic import TemplateView

from authentication.views import AuthenticationView, LoginView, logout_view

urlpatterns = [
	url(r'^$', LoginView.as_view(), name="login_screen"),
    url(r'/(?P<error_code>[0-9]+)/$', LoginView.as_view(), name="login_error"),
    url(r'^authenticate/', AuthenticationView.as_view(), name="authenticate"),
    url(r'^logout', logout_view, name="logout_user"),
]