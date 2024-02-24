from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from books.views import LoginView, LogoutView, RegistrationView


schema_view = get_schema_view(
    openapi.Info(
        title = "Book Giveaway",
        default_version="v1",
        description="Book Giveaway Service where registered users can offer books for free and also take books that are offered by others.",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('api/', include('books.urls')),
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
