from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

@method_decorator(login_required, name='dispatch')
class CustomUserListView(ListView):
    model = CustomUser
    template_name = 'customuser_list.html'
    context_object_name = 'users'

@method_decorator(login_required, name='dispatch')
class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'customuser_form.html'
    success_url = reverse_lazy('user-list')

@method_decorator(login_required, name='dispatch')
class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'customuser_form.html'
    success_url = reverse_lazy('user-list')

@method_decorator(login_required, name='dispatch')
class CustomUserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'customuser_confirm_delete.html'
    success_url = reverse_lazy('user-list')
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Log the user in after registration
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('user-login')  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class UserLoginForm(View):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password,)
            if user is not None:
                login(request, user)
                return redirect('home') 

        return render(request, 'registration/login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('user-register')
