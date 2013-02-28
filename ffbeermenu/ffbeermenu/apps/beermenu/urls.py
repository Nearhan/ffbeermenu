from django.conf.urls import patterns, include, url
from ffbeermenu.apps.beermenu.views import BeerMenuView

urlpatterns = patterns('',
    url(r'^$', BeerMenuView.as_view()),)