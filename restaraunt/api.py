from django.views.generic import TemplateView
from django.http.response import HttpResponse
import json
from django.utils import timezone

from restaraunt import models

class DishOrder(TemplateView):
    def post(self, request, **kwargs):
        data = json.loads(request.body.decode("utf-8"))
        id = int(kwargs.get('id', None))
        obj = models.Order()
        obj.dish_id = id

        # if order if made for tomorrow set date = tomorrow
        if data['order']:
            obj.date = timezone.now() + timezone.timedelta(days=1)
        obj.save()
        return HttpResponse({}, content_type="application/json")
