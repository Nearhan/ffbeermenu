from django.db import models
from django_countries import CountryField
# Create your models here.


class Menu(models.Model):

    def __unicode__(self):
        return u'Beer Menu'


class Beer(models.Model):
    TYPES_OF_BEER = (
        ('L', 'Lager'),
        ('I', 'IPA'),
        ('W', 'White'),
        ('A', 'Ale'),
        ('S', 'Seasonal'),
        ('Lo', 'Local'),
    )
    menu = models.ForeignKey(Menu)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=2, choices=TYPES_OF_BEER)
    location = CountryField()
    price_of_4oz = models.FloatField(max_length=3)
    price_of_glass = models.FloatField(max_length=3)
    abv = models.FloatField(max_length=3)
    position = models.PositiveSmallIntegerField('Position')

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        return u'%s' % self.name

    def display(self):
        output = '{0} | {1} | {2} | {3}'.format(self.type, self.name,
                                                self.location, self.abv)
        return output

    def display_price(self):
        output = '{0} | {1}'.format(self.price_of_4oz, self.price_of_glass)
        return output


