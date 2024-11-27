from django.shortcuts import render
from rest_framework import viewsets
from users.models import CustomUser
from users.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from django.contrib.auth import login, authenticate, logout
import logging
logger = logging.getLogger(__name__)



class RegisterUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            },  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    
    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # user = CustomUser.objects.get(username=username, password=password)
        user = authenticate(request, username=username, password=password)

        
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            userData = {
                "user_id": user.id,
                "username": user.username,
                "token": token.key
            }

            return Response({"message": "Login successful", "data": userData}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

class ProfileDataViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def retrieve(self, request, pk=None):
        try:
            user = CustomUser.objects.get(pk=pk)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
