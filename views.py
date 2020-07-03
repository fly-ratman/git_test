from django.http import HttpResponse

def index(request):
	return HttpResponse('helloworld')

def login(request):
	return Redirect('/index')