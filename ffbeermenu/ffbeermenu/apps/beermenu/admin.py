from django.contrib import admin
from ffbeermenu.apps.beermenu.models import Menu, Beer, BeerType

class BeerInlineAdmin(admin.StackedInline):
    model= Beer
    extra = 0
    sortable_field_name = 'position'

class MenuAdmin(admin.ModelAdmin):
    inlines = [BeerInlineAdmin]

class BeerTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Menu, MenuAdmin)
admin.site.register(BeerType, BeerTypeAdmin)
