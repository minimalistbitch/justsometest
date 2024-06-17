from django.urls import path
from .views import (
    CustomUserListView,
    CustomUserCreateView,
    CustomUserUpdateView,
    CustomUserDeleteView,
    UserLoginForm,
    register,
    home,
    logout_view
)

urlpatterns = [
    path('users/', CustomUserListView.as_view(), name='user-list'),
    path('users/create/', CustomUserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', CustomUserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', CustomUserDeleteView.as_view(), name='user-delete'),
    path('user/login/', UserLoginForm.as_view(), name='user-login'),
    path('register/', register, name='user-register'),
    path('user/login/home/', home, name='home'),
    path('user/login/home/logout', logout_view, name='logout')

]
