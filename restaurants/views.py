from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView
from .models import RestaurantLocation
from django.shortcuts import render, get_object_or_404

# Create your views here.


class RestaurantListView(ListView):
    context_object_name = 'queryset'
    def get_queryset(self):

        slug = self.kwargs.get('slug')
        qs = RestaurantLocation.objects.all()
        if slug:
            queryset = RestaurantLocation.objects.filter(
                                Q(category__iexact=slug)
                                | Q(category__icontains=slug))
        else:
            queryset = qs

        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(RestaurantLocation, id=rest_id) # pk = rest_id
        return obj





