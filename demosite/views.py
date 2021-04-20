from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>home page</h1>')