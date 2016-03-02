from django.conf.urls import url
from django.views.generic import TemplateView

from authentication.views import AuthenticationView, LoginView

urlpatterns = [
	url(r'^$', LoginView.as_view(), name="login_screen"),
    url(r'/(?P<error_code>[0-9]+)/$', LoginView.as_view(), name="login_error"),
    url(r'^authenticate/', AuthenticationView.as_view(), name="authenticate"),
]