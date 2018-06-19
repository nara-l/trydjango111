from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.

# function based view

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['body'] = "Body content for home"
        return context

