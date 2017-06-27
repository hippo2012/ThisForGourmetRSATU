from django.contrib import admin

from . import models

class dishAdmin(admin.ModelAdmin):
    model = models.Dish
    filter_horizontal = ('ingredient',)

admin.site.register(models.Ingredient)
admin.site.register(models.Dish, dishAdmin)
admin.site.register(models.Storage)
admin.site.register(models.Consist)
admin.site.register(models.Order)
