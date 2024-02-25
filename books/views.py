
from rest_framework import viewsets, filters, status
from books.filters import BookFilter, CustomSearchFilter
from rest_framework.filters import OrderingFilter
from .models import Book, WishList
from .serializers import BookSerializer, WishListSerializer, UserRegistrationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from .permissions import  WishListPermission, IsOwnerOrStaffForPatch
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout


# Books' titles
class BookViewSet(viewsets.ModelViewSet): 
    queryset = Book.objects.all()   
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, CustomSearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author__name', 'genre__name', 'condition__name', 'owner__username']



class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

    def get_permissions(self):
        if self.action == 'partial_update':
            permission_classes = [IsOwnerOrStaffForPatch]
        else:
            permission_classes = [IsAuthenticated]
            print("i")
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

# Registration
class RegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'user': serializer.data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Authorisation 
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

# Logout
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Get the user's token
        logout(request)
        return Response({'message': 'User logged out successfully.'}, status=status.HTTP_200_OK)
