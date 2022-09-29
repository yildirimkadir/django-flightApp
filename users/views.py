from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # token = Token.objects.create(user=user)
        token = Token.objects.get(user=user)
        data = serializer.data
        data['token'] = token.key
        data["message"] = "user created successfully"
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
    

# Create your views here.
