from django.views.generic import TemplateView, View

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