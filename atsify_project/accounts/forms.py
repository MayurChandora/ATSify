from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User

TAILWIND_CLASS = 'w-full px-4 py-3 bg-slate-900/50 border border-slate-700/50 rounded-xl text-slate-200 focus:outline-none focus:ring-2 focus:ring-brand-primary focus:border-transparent transition-all duration-200 font-mono text-sm shadow-inner'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'full_name')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': TAILWIND_CLASS})

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': TAILWIND_CLASS})

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name',)
