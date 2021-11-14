from django.views.generic import TemplateView
from rest_framework import viewsets

from todos.models import Todo
from todos.serializers import TodoSerializer



class VueTodoTemplateView(TemplateView):
    template_name = "todos/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["first_message"] = "Hello Vue.js in Django Template!"
        context["even_numbers"] = [x for x in range(11) if x % 2 == 0]
        return context


class TodoViewset(viewsets.ModelViewSet):

    queryset = Todo.objects.all().order_by("id")
    serializer_class = TodoSerializer
