from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {
        "welcome_message": "Welcome to SaaSBoard! Your platform for building SaaS with Django.",
        "subtitle": "Get started by exploring our features and documentation."
    }
    return render(request, 'home.html', context)