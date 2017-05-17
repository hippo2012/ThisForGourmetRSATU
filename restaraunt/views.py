from django.shortcuts import render

from django.views.generic import TemplateView, View
from . import models

class IndexView(TemplateView):
    model = models.Dish
    template_name = "front/Index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['dishes'] = self.model.objects.all()

        return context
