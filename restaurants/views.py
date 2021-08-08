from django.views.generic import ListView, DetailView, TemplateView

from .models import Rating, Restaurant


# class RestaurantsListView(ListView):
class RestaurantsListView(TemplateView):
    model = Restaurant
    template_name = 'restaurants/list.html'

    def get_queryset(self):
        return Restaurant.objects.filter()


class RestaurantsDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurants/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rating_dict = dict(zip(Rating.values, Rating.labels))
        rating = rating_dict[self.object.rating]
        context['rating'] = rating
        return context
