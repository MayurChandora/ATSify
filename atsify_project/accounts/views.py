from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserUpdateForm, CustomAuthenticationForm
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    form_class = CustomAuthenticationForm
    
    def get_success_url(self):
        return reverse_lazy('home')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    if request.method == 'POST':
        if 'update_profile' in request.POST:
            p_form = UserUpdateForm(request.POST, instance=request.user)
            pw_form = PasswordChangeForm(request.user)
            if p_form.is_valid():
                p_form.save()
                messages.success(request, "Your profile has been updated!")
                return redirect('profile')
        elif 'change_password' in request.POST:
            p_form = UserUpdateForm(instance=request.user)
            pw_form = PasswordChangeForm(request.user, request.POST)
            if pw_form.is_valid():
                user = pw_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Your password was successfully updated!")
                return redirect('profile')
            else:
                messages.error(request, "Please correct the errors below.")
    else:
        p_form = UserUpdateForm(instance=request.user)
        pw_form = PasswordChangeForm(request.user)

    tailwind_class = 'w-full px-4 py-3 bg-slate-900/50 border border-slate-700/50 rounded-xl text-slate-200 focus:outline-none focus:ring-2 focus:ring-brand-primary focus:border-transparent transition-all duration-200 font-mono text-sm shadow-inner'
    for field in p_form.fields.values():
        field.widget.attrs.update({'class': tailwind_class})
    for field in pw_form.fields.values():
        field.widget.attrs.update({'class': tailwind_class})

    context = {
        'p_form': p_form,
        'pw_form': pw_form
    }
    return render(request, 'accounts/profile.html', context)
