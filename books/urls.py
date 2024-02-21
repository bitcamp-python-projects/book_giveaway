from django.urls import path, include
from .views import BookViewSet, WishListViewSet, LoginView, LogoutView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'booklist', BookViewSet, basename="booklist"),
router.register(r'wishlist', WishListViewSet, basename="wishlist"),


urlpatterns = [
    path('', include(router.urls)),
]
