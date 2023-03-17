from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from users.models import User
from products.models import Basket
from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('index')




class UserRegistration(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class UserProfileView(UpdateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:login')

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


def profile(request):
    context = {'form': UserProfileForm()}
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
