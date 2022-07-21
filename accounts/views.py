from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'accounts/login.html')


def register_view(request):
    return render(request, 'accounts/register.html')