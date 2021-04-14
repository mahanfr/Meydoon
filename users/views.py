from django.shortcuts import redirect, render
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRrgisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            return redirect('login')
    else:
        form = UserRrgisterForm()
    return render(request,'users/register.html',{'form':form})
