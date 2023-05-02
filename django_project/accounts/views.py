from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {
        'form': form,
    })
