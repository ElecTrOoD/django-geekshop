from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from baskets.models import Basket
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from users.models import User


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')
    redirect_authenticated_user = True
    extra_context = {'title': 'GeekShop - авторизация'}


class UserRegisterView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    extra_context = {'title': 'GeekShop - регистрация'}

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'Вы успешно зарегистрировались!\nАвторизуйтесь для продолжения.')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class UserProfileUpdateView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'Профиль отредактирован!')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(UserProfileUpdateView, self).get_context_data(**kwargs)
        user = self.get_object()
        context['title'] = f'GeekShop - профиль {user.username}'
        context['baskets'] = Basket.objects.filter(user=user.id)
        return context


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')
