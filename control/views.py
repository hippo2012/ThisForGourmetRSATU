from django.views.generic import TemplateView, View
from django.utils import timezone

from restaraunt import models


class IndexView(TemplateView):
    template_name = "control/Index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        dishes = models.Dish.objects.all()
        context['dishes'] = []

        for dish in dishes:
            ingredients = models.Consist.objects.filter(dish=dish.id)

            # dish and it`s ingredients
            obj = {'name': dish.name,
                   'id': dish.id,
                   'ingredients': [{'name': models.Ingredient.objects.get(id=i.ingredient_id).name,
                                    'count': i.count} for i in ingredients]}
            context['dishes'].append(obj)

        context['ingredients'] = models.Ingredient.objects.all()

        return context


class IngredientsView(TemplateView):
    template_name = "control/Ingredients.html"

    def get_context_data(self, **kwargs):
        context = super(IngredientsView, self).get_context_data(**kwargs)
        context['ingredients'] = models.Ingredient.objects.all()

        return context

class OrdersView(TemplateView):
    template_name = "control/Orders.html"

    def get_context_data(self, **kwargs):
        context = super(OrdersView, self).get_context_data(**kwargs)

        id = kwargs.get('id', None)
        if id:
            id = int(id)

        if id == 1: #today
            dishes = models.Order.objects.filter(date=timezone.now())
        elif id == 2: #tomorrow
            dishes = models.Order.objects.filter(date=timezone.now() + timezone.timedelta(days=1))

        context['dishes'] = [models.Dish.objects.get(id = d.dish_id) for d in dishes]

        return context