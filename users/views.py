from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm
from users.models import CustomUser


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в Love Flowers'
        message = 'Спасибо, что зарегистрировались в нашем интернет-магазине! Будем рады сотрудничать.'
        from_email = 'my.nik.mariann@gmail.com'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('catalog:product_list')


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserProfileForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('users:profile_edit')

    def get_object(self, queryset=None):
        return self.request.user
