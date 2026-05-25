from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name", widget=forms.TextInput(attrs={'placeholder': 'John Doe'}))
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={'placeholder': 'john@example.com'}))
    subject = forms.CharField(max_length=200, label="Subject", widget=forms.TextInput(attrs={'placeholder': 'How can we help?'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your message here...', 'rows': 5}), label="Message")
