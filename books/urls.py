from django.urls import path, include
from .views import BookViewSet, BookDetailViewSet, WishListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'booklist', BookViewSet, basename="list"),
router.register(r'book', BookDetailViewSet,  basename="books"),
router.register(r'wishlist', WishListViewSet),

urlpatterns = [
    path('', include(router.urls)),
]
