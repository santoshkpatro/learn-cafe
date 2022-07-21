from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def login_view(request):
    # print(request.method)
    if request.method == 'POST':
        print(request.POST)
        # return redirect('/')
    return render(request, 'accounts/login.html')


def register_view(request):
    return HttpResponse('register')