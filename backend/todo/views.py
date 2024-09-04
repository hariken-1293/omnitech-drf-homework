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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class TodoItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def protected_view(request):
#     return Response({"message": "This is a protected view!"})
