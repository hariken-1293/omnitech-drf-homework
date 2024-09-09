from django.test import TestCase

# Create your tests here.
# backend/todo/tests/test_models.py
import pytest
from django.utils import timezone
from todo.models import TodoItem


@pytest.mark.django_db
def test_todo_item_creation():
    todo = TodoItem.objects.create(
        title="Test Todo", description="Test Description", completed=False
    )
    assert todo.title == "Test Todo"
    assert todo.description == "Test Description"
    assert todo.completed is False


@pytest.mark.django_db
def test_todo_item_str_method():
    todo = TodoItem.objects.create(title="Test Todo")
    assert str(todo) == "Test Todo"


@pytest.mark.django_db
def test_todo_item_default_values():
    todo = TodoItem.objects.create(title="Test Todo")
    assert todo.description is None
    assert todo.completed is False
