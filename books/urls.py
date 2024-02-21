from django.urls import path, include
from .views import BookViewSet, BookDetailViewSet, WishListViewSet, LoginView, LogoutView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'booklist', BookViewSet, basename="booklist"),
router.register(r'book', BookDetailViewSet,  basename="books"),
router.register(r'wishlist', WishListViewSet, basename="wishlist"),


urlpatterns = [
    path('', include(router.urls)),
]
