from django.urls import path
from django.views.decorators.cache import cache_page

from users.views import UserLoginView, UserLogoutView, UserRegisterView, UserProfileUpdateView, verify

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', cache_page(3600)(UserProfileUpdateView.as_view()), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('verify/<email>/<activation_key>/', verify, name='verify'),
]
