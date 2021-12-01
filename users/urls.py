from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.UserRegisterationAPIView.as_view(),
         name="create_user"),
    path('login/', views.UserLoginAPIView.as_view(), name="login_user"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.UserLogoutAPIView.as_view(), name='logout_user')
]
