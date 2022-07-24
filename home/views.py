from django.shortcuts import render, redirect
from .models import Contact

def index(request):
    # Processing
    data = {
        'full_name': 'Santosh',
        'age': 19,
        'marks': [10, 20, 30]
    }
    return render(request, 'home/index.html', data)


def about_us(request):
    return render(request, 'home/about.html')


def contact_us(request):
    if request.method == 'POST':
        # print(request.POST)
        # print('Name: ', request.POST['name'])
        # print('Email: ', request.POST['email'])
        # print('Message: ', request.POST['message'])

        # DB save
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # Method 1
        # contact = Contact.objects.create(name=name, email=email, phone=phone, message=message)

        # Methhod 2
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()

        return redirect('index')

    return render(request, 'home/contact.html')
