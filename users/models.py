from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.urls import reverse


class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True, max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['phone_number', 'username', 'first_name',
                       'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
'''
def get_absolute_url(self):
        return reverse('login', args=[str(self.id)])
'''

  


   
'''

from django.contrib import admin
from .models import User

# Register your models here.
admin.site.register(User)
'''


'''
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm, CustomUserChangeForm


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:profile')
        else:
            err = form.errors.as_data()
            print(err)
            bag = []
            for key in err:
                str1 = " "
                val = err[key]
                bag.append(str1.join(val[0]))
            return render(request, 'accounts/registration.html', {'errors': bag})
    else:
        form = CustomUserCreationForm()
        return render(request, "accounts/registration.html", {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('accounts:profile')
        else:
            message = form.errors.as_data().get('__all__')[0]
            return render(request, 'accounts/login.html', {'message': message})
    else:
        form = CustomUserAuthenticationForm()
    return render(request, "accounts/login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def profile_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('accounts:profile')
        else:
            print(form.errors.as_data())
            return render(request, 'accounts/edit_profile.html', {'form': form})
    else:
        form = CustomUserChangeForm(instance=request.user)
        return render(request, "accounts/edit_profile.html", {'form': form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/change_pass.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('accounts:profile')

'''


