from django.shortcuts import render

from django.views.generic import TemplateView, View
from restaraunt import models

class IndexView(TemplateView):
    template_name = "control/Index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['dishes'] = models.Dish.objects.all()

        return context

