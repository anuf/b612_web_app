from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'b612_web_app/home.html')


def services(request):
    return render(request, 'b612_web_app/services.html')


def shop(request):
    return render(request, 'b612_web_app/shop.html')


def blog(request):
    return render(request, 'b612_web_app/blog.html')


def contact(request):
    return render(request, 'b612_web_app/contact.html')


def about(request):
    return render(request, 'b612_web_app/about.html')