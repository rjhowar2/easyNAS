from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class AuthenticationView(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(AuthenticationView, self).dispatch(*args, **kwargs)

	def post(self, request, *args, **kwargs):
		password = request.POST.get('password','wak')
		email = request.POST.get('email','fuvk')

		if password == 'reezy':
			return HttpResponse('Success', status=200)
		else:
			return HttpResponse('Unauthorized', status=401)

class LoginView(TemplateView):

	template_name='authentication/login.html'