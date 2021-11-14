from django.urls import path
from rest_framework import routers
from todos.views import VueTodoTemplateView, TodoViewset

app_name = "todos"

router = routers.DefaultRouter()

router.register(r"todos", TodoViewset)

urlpatterns = [
    path("list/", VueTodoTemplateView.as_view(), name="todo_index"),
]

urlpatterns += router.urls