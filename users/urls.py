from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserLoginView, UserProfileUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit'),

]
