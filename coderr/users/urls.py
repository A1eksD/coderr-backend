from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import RegisterUserViewSet, LoginViewSet, ProfileDataViewSet


router = DefaultRouter()
router.register(r'registration', RegisterUserViewSet, basename='registration')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'profile', ProfileDataViewSet, basename='profile')

all_name = 'users'

urlpatterns = [
    path('', include(router.urls)),
]