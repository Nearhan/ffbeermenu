# Create your views here.
from django.views.generic import TemplateView
from ffbeermenu.apps.beermenu.models import Menu

class BeerMenuView(TemplateView):
    template_name = 'beermenu/menu.html'

    def get_context_data(self, **kwargs):
        context = super(BeerMenuView, self).get_context_data(**kwargs)
        menu = Menu.objects.all()[0]
        context['object'] = menu.beer_set.order_by('position')
        return context




