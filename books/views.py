from rest_framework import viewsets, filters, status
from .models import Book, WishList
from .serializers import BookSerializer, BookDetailSerializer, WishListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from .permissions import  WishListPermission, IsOwnerOrAdministrator
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# წიგნების სახელწოდებები
class BookViewSet(viewsets.ReadOnlyModelViewSet): # ეს ვიუსეტი მარტო კითხვის ფუნქციას რთავს, ამას თუ დავწერთ ფერმიშენი არც დაგვჭირდება
    queryset = Book.objects.all()   #ეს ვიუსეტი ხომ მარტო უნდა გამოიტანოს ლისტის სახით ყველასთვის ხელმისაწვდომად
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly] # ამიტომ ეს ველი აღარ დაგვჭირდება
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author', 'genre', 'condition', 'owner']
    search_fields = ['title']

# წიგნების შესახებ სრული ინფორმაცია
class BookDetailViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [IsOwnerOrAdministrator]
    authentication_classes=[TokenAuthentication]

# სასურველი წიგნების ცრილი
class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [WishListPermission] #სპეციალური პერმიშენი ვიშლისტისთვის


# ავტორიზაცია მეილით
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
