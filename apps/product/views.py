from django.shortcuts import render, get_object_or_404

from .models import Product, Category  # ProductImage
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from django.template import context


class HomePageView(TemplateView):

    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["current_category"] = None
        return context
