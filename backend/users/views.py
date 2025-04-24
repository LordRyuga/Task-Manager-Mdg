from django.shortcuts import render
from rest_framework import status, views, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import userRegisterationSerializer
from .models import CustomUser

class UserViewSet(viewsets.GenericViewSet):

    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        print(request.data)
        serializer = userRegisterationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'], permission_classes = [permissions.IsAuthenticated])
    def get_user(self, request):
        user = request.user
        serializer = userRegisterationSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

