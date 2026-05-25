from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def index_view(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')  # The dashboard placeholder
    return render(request, 'pages/landing.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # In a real app, send email here
            messages.success(request, "Thank you for your message! We'll get back to you shortly.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})
