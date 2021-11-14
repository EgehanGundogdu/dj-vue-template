from django.http import response
from django.views.generic import TemplateView
import random


class VueView(TemplateView):
    template_name = "vue_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        names = ["John", "Jack", "William", "Guido"]
        persons = [
            {"name": random.choice(names), "age": random.randint(10, 50)}
            for _ in range(5)
        ]
        context["persons"] = persons
        return context
