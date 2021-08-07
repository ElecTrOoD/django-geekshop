from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from baskets.models import Basket
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm, UserSocialProfileForm
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
    success_message = 'Вы успешно зарегистрировались!\n' \
                      'Ссылка для активации аккаунта и авторизации отправлена на ваш email.'

    def form_valid(self, form):
        self.object = form.save()
        if send_verify_mail(self.object):
            print('success sending')
            messages.success(self.request, self.success_message)
        else:
            print('sending fail')
        return HttpResponseRedirect(self.get_success_url())


class UserProfileUpdateView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    success_message = 'Профиль отредактирован!'

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        profile_form = UserProfileForm(self.request.POST, self.request.FILES, instance=user)
        social_profile_form = UserSocialProfileForm(self.request.POST, instance=user.userprofile)
        if profile_form.is_valid() and social_profile_form.is_valid():
            profile_form.save()
            messages.success(request, self.success_message)
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            return self.form_invalid(profile_form)

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        user = self.get_object()
        profile_form = UserProfileForm(instance=user)
        social_profile_form = UserSocialProfileForm(instance=user.userprofile)
        context = {'title': f'GeekShop - профиль {user.username}',
                   'baskets': Basket.objects.filter(user=user.id),
                   'profile_form': profile_form,
                   'social_profile_form': social_profile_form}
        return context


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')


def verify(request, email, activation_key):
    user = User.objects.filter(email=email).first()
    if user:
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'users/verify.html')
    return HttpResponseRedirect(reverse('index'))


def send_verify_mail(user):
    subject = 'Verify your account'
    link = reverse('users:verify', args=[user.email, user.activation_key])
    message = f'Для подтверждения учетной записи {user.username} перейдите по ссылке: {settings.DOMAIN}{link}'
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
