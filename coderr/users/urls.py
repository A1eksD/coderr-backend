from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import RegisterUserViewSet, LoginViewSet, ProfileDataViewSet, LogoutView


router = DefaultRouter()
router.register(r'registration', RegisterUserViewSet, basename='registration')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'profile', ProfileDataViewSet, basename='profile')
router.register(r'logout', LogoutView, basename='logout')

all_name = 'users'

urlpatterns = [
    path('', include(router.urls)),
]