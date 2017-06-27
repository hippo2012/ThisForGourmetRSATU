from django.views.generic import TemplateView
from django.http.response import HttpResponse
import json
import xlwt
from restaraunt import models


class Dish(TemplateView):
    def post(self, request, **kwargs):
        data = json.loads(request.body.decode("utf-8"))
        id = kwargs.get('id', None)
        if id:
            id = int(id)
            obj = models.Dish.objects.get(id=id)
            for consist in models.Consist.objects.filter(dish_id=id):
                consist.delete()
        else:
            obj = models.Dish()

        obj.name = data['name']
        obj.price = int(data['price'])
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


class Ingredient(TemplateView):
    def post(self, request, **kwargs):
        data = json.loads(request.body.decode("utf-8"))

        id = kwargs.get('id', None)
        if id:
            id = int(id)
            obj = models.Ingredient.objects.get(id=id)
        else:
            obj = models.Ingredient()

        obj.name = data['name']
        obj.save()

        return HttpResponse({}, content_type="application/json")

    def delete(self, request, **kwargs):
        id = int(kwargs.get('id', None))
        obj = models.Ingredient.objects.get(id=id)
        obj.delete()

        return HttpResponse({}, content_type="application/json")


def menu_export(request):
    response = HttpResponse(content_type='application/ms-excel')

    response['Content-Disposition'] = 'attachment; filename="menu.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Menu')

    # Sheet header, first row
    row_num = 0

    dishes = models.Dish.objects.all()
    rows = []

    for dish in dishes:
        ingredients = models.Consist.objects.filter(dish=dish.id)
        has_ingredients = True

        for ingredient in ingredients:
            if get_ingredient_count(ingredient.ingredient) < ingredient.count:
                has_ingredients = False

        if has_ingredients:
            # dish and it`s ingredients
            obj = {'name': dish.name, 'price': dish.price,
                   'ingredients': [models.Ingredient.objects.get(id=i.ingredient_id).name for i in ingredients]}
            rows.append(obj)

    for row in rows:
        ws.write(row_num, 0, u'Dish')
        ws.write(row_num, 1, row['name'])
        row_num += 1
        ws.write(row_num, 0, u'Price')
        ws.write(row_num, 1, row['price'])
        row_num += 1
        ws.write(row_num, 0, u'Ingredients')
        col_num = 1

        for ingr in row['ingredients']:
            ws.write(row_num, col_num, ingr)
            col_num += 1

        row_num += 1

    wb.save(response)
    return response

def ingredients_export(request):
    response = HttpResponse(content_type='application/ms-excel')

    response['Content-Disposition'] = 'attachment; filename="ingredients.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Ingredients')

    # Sheet header, first row
    row_num = 0

    rows = models.Ingredient.objects.all()

    for row in rows:
        ws.write(row_num, 0, u'Name')
        ws.write(row_num, 1, row.name)
        row_num += 1

    wb.save(response)
    return response


def get_ingredient_count(ingredient_id):
    count = 0

    for item in models.Storage.objects.filter(ingredient=ingredient_id):
        count += item.count

    return count
