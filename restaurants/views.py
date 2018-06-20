from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.


def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    context = {'object_lists': [1,2,3,455,]}
    return render(request, template_name, context)
