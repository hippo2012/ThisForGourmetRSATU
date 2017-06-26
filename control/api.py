from django.views.generic import TemplateView
from django.http.response import HttpResponse
import json
from restaraunt import models

class Dish(TemplateView):
    def post(self, request, **kwargs):
        data = json.loads(request.body.decode("utf-8"))
        id = int(kwargs.get('id', None))
        if id:
            pass
        else:
            obj = models.Dish()
            obj.name = data['name']
            obj.save()
            for ingredient in data['ingredients']:
                consist = models.Consist()
                consist.dish_id = obj.id
                consist.ingredient_id = models.Ingredient.objects.get(name=ingredient['name']).id
                consist.count = int(ingredient['count'])
                consist.save()

        return HttpResponse({}, content_type="application/json")

    def delete(self, request, **kwargs):
        id = int(kwargs.get('id', None))
        obj = models.Dish.objects.get(id=id)
        obj.delete()

        return HttpResponse({}, content_type="application/json")
