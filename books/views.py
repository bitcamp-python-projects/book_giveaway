
from rest_framework import viewsets, filters, status
from .models import Book, WishList
from .serializers import BookSerializer, BookDetailSerializer, WishListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from .permissions import  WishListPermission, IsOwnerOrStaffForPatch
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout


# წიგნების სახელწოდებები
class BookViewSet(viewsets.ReadOnlyModelViewSet): 
    queryset = Book.objects.all()   
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author', 'genre', 'condition', 'owner']
    search_fields = ['title']

# წიგნების შესახებ სრული ინფორმაცია
class BookDetailViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes=[TokenAuthentication]

# სასურველი წიგნების ცრილი


class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

    def get_permissions(self):
        if self.action == 'partial_update':
            permission_classes = [IsOwnerOrStaffForPatch]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk=None):
        wishlist = self.get_object()
        serializer = self.get_serializer(wishlist)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        wishlist = self.get_object()
        serializer = self.get_serializer(wishlist, data=request.data, partial=True)
        if serializer.is_valid():
            if wishlist.book.owner == request.user or request.user.is_staff:
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ავტორიზაცია მეილით
class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]  # Add TokenAuthentication

    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Authenticate user
        
        user = authenticate(username=username, password=password)
    
        
        if user:
            # Generate or retrieve token
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Get the user's token

        logout(request)
        return Response({'message': 'User logged out successfully.'}, status=status.HTTP_200_OK)
