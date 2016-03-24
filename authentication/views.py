from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class AuthenticationView(View):

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard_home'))
            else:
                error_code = 200
        else:
            error_code = 300

        return HttpResponseRedirect(reverse('login_error', kwargs = {'error_code': error_code}))

class LoginView(TemplateView):

    template_name='authentication/login.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)

        if "error_code" in kwargs:
            context["error_message"] = LOGIN_ERRORS[kwargs["error_code"]]

        return context

def logout_view(request):
    logout(request)
    # Redirect to a success page.

LOGIN_ERRORS = {
    200: "This accounthas been disabled. Please contact the administrator.",
    300: "There was an error with your E-Mail/Password combination. Please try again."
}