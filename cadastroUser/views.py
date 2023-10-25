
from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

from .models import UsuarioComum
from .serializers import UsuarioComumSerializer, LoginSerializer

#Usuario que será cadastrado
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = UsuarioComum.objects.all()
    serializer_class = UsuarioComumSerializer
    permission_classes = [permissions.DjangoObjectPermissions]

#login
class LoginView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
           
            if user is not None:
                login(request, user)
                # Retorne um token ou informações de usuário para indicar que o login foi bem-sucedido
                return Response({'message': 'Login bem-sucedido'})
        # Retorne uma resposta de erro se o login falhar
        return Response({'message': 'Login falhou'}, status=status.HTTP_401_UNAUTHORIZED)