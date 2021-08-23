from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Project


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        projects = Project.objects.order_by("-pub_date")
        return render(request, self.template_name, {"projects": projects})
