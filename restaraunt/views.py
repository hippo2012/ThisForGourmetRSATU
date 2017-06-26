from django.shortcuts import render

from django.views.generic import TemplateView, View
from . import models

class IndexView(TemplateView):
    template_name = "front/Index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        dishes = models.Dish.objects.all()
        context['dishes'] = []

        for dish in dishes:
            ingredients = models.Consist.objects.filter(dish=dish.id)
            has_ingredients = True

            for ingredient in ingredients:
                if get_ingredient_count(ingredient.ingredient) < ingredient.count:
                    has_ingredients = False

            if has_ingredients:
                # dish and it`s ingredients
                obj = {'name': dish.name, 'ingredients': [models.Ingredient.objects.get(id=i.ingredient_id).name for i in ingredients]}
                context['dishes'].append(obj)

        return context

class OrderView(TemplateView):
    template_name = "front/Order.html"

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        dishes = models.Dish.objects.all()
        context['dishes'] = []

        for dish in dishes:
            ingredients = models.Consist.objects.filter(dish=dish.id)
            has_ingredients = False

            for ingredient in ingredients:
                if get_ingredient_count(ingredient.ingredient_id) >= ingredient.count:
                    has_ingredients = True

            if has_ingredients:
                # dish and it`s ingredients
                obj = {'name': dish.name, 'ingredients': [models.Ingredient.objects.get(id=i.ingredient_id).name for i in ingredients]}
                context['dishes'].append(obj)

        return context

def get_ingredient_count(ingredient_id):
    count = 0

    for item in models.Storage.objects.filter(ingredient=ingredient_id):
        count += item.count

    return count
