from django.urls import path
from .views import RegisterUserView,RoleManagementView,ProtectedView,api_tester
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('roles/', RoleManagementView.as_view(), name='roles'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tester/', api_tester, name='api_tester'),
]
