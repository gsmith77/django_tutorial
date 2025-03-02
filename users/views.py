from django.http import HttpResponse

def all_users(request):
    return HttpResponse('All users.')