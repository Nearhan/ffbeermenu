from django.db import models
from ffbeermenu.apps.beermenu.utils import LOCATIONS
# Create your models here.


class Menu(models.Model):

    def __unicode__(self):
        return u'Beer Menu'

class BeerType(models.Model):
    type_name = models.CharField(max_length=35)

    def __unicode__(self):
        return self.type_name


class Beer(models.Model):
    
    menu = models.ForeignKey(Menu)
    name = models.CharField(max_length=35)
    beer_type = models.ForeignKey(BeerType)
    location = models.CharField(max_length=3, choices=LOCATIONS)
    price_of_4oz = models.CharField(max_length=5)
    price_of_glass = models.CharField(max_length=5)
    abv = models.CharField(max_length=5)
    position = models.PositiveSmallIntegerField('Position')

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        output = '{0} | {1} | {2} | {3}'.format(self.beer_type.type_name, self.name,
                                                self.location, self.abv)
        return output

    def display(self):
        output = '{0} | {1} | {2} | {3}%'.format(self.beer_type.type_name, self.name,
                                                self.location, self.abv)
        return output

    def display_price(self):
        output = '{0} | {1}'.format(self.price_of_4oz, self.price_of_glass)
        return output

