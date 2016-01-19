from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

class AuthenticationView(View):

    def post(self, request, *args, **kwargs):
    	password = request.POST.get('password','wak')
        email = request.POST.get('email','fuvk')

        if password == 'reezy':
        	return HttpResponse('Success', status=200)
        else:
			return HttpResponse('Unauthorized', status=401)
