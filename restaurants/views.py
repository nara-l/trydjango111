from django.shortcuts import render


# Create your views here.

# function based view

def home(request):
    template_name = 'home.html'

    return render(request, template_name, {'body': "home page body content here"})


def about(request):
    template_name = 'about.html'

    return render(request, template_name, {'body': "about us body content here"})


def contact(request):
    template_name = 'contact.html'

    return render(request, template_name, {'body': "Contact us body content"
                                                   " here"})
