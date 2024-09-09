from django.urls import path
from .views import (
    TodoItemListCreateView,
    TodoItemRetrieveUpdateDestroyView,
    UserTodoListView,
)

urlpatterns = [
    path("todos/", TodoItemListCreateView.as_view(), name="todo-list-create"),
    path(
        "todos/<int:pk>/",
        TodoItemRetrieveUpdateDestroyView.as_view(),
        name="todo-detail",
    ),
    path("my-todos/", UserTodoListView.as_view(), name="user-todo-list"),
]
