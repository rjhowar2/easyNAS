"""easyNAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from dashboard.views import DashboardView
from authentication.views import AuthenticationView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('login_screen'))),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', TemplateView.as_view(template_name='authentication/login.html'), name="login_screen"),
    url(r'^login/authenticate/$', csrf_exempt(AuthenticationView.as_view()), name="authenticate"),
    url(r'^home/$', DashboardView.as_view(), name="nas_home"),
]

urlpatterns += staticfiles_urlpatterns()