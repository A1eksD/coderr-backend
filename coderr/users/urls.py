from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import RegisterUserViewSet


router = DefaultRouter()
router.register(r'registration', RegisterUserViewSet, basename='registration')

all_name = 'users'

urlpatterns = [
    path('', include(router.urls)),
]