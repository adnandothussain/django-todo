from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos, name="todos"),
    path('delete/<str:id>', views.delete_todo, name="delete_todo"),
    path('update/<str:id>', views.update_todo, name="update_todo")
]
