from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from verify_email.email_handler import send_verification_email

from .forms import CustomUserCreationForm


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            return render(request, 'accounts/registration_redirect.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {
        'form': form,
    })


@login_required
def logout_view(request):
    logout(request)
    return redirect('core:index')
