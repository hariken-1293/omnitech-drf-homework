from django.shortcuts import render
from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication


class TodoItemListCreateView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]


class TodoItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class UserTodoListView(generics.ListAPIView):
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]  # 認証済みユーザのみアクセス可能

    def get_queryset(self):
        # 認証されたユーザのTodoのみ取得
        return TodoItem.objects.filter(user=self.request.user)
