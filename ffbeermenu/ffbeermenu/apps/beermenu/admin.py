from django.contrib import admin
from ffbeermenu.apps.beermenu.models import Menu, Beer

class BeerInlineAdmin(admin.StackedInline):
    model= Beer
    extra = 0
    sortable_field_name = 'position'

class MenuAdmin(admin.ModelAdmin):
    inlines = [BeerInlineAdmin]

admin.site.register(Menu, MenuAdmin)