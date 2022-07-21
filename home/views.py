from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('Hello')


def about_us(request):
    return HttpResponse('About Us Page')
