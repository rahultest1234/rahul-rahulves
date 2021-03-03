from django.http import HttpResponse


def index(request):
    user_name = request.GET.get('user_name', '')
    return HttpResponse("Hello, My Name is " + user_name+user_name)
