from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from users.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request == 'POST':
        forms = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.htnl', {'from': form })

@login_required
def profile(request):
    return redirect(request, 'users/profile.html')