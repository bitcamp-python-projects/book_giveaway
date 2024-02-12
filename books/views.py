from rest_framework import viewsets, permissions
from .models import Book, WishList
from .serializers import BookSerializer, BookDetailSerializer, WishListSerializer


# წიგნების სახელწოდებები
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# წიგნების შესახებ სრული ინფორმაცია
class BookDetailViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# სასურველი წიგნების ცრილი
class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    # permission_classes = [permissions.IsAuthenticated]
