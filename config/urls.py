from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', CreateUserView.as_view(), name='register'), # User registration endpoint 【1569.12, type: source】 
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'), # Endpoint to get JWT tokens 【1569.12, type: source】 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh'), # Endpoint to refresh JWT tokens 【1569.12, type: source】 
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')), # Includes URLs from the 'api' app 【2774.8, type: source】 
]