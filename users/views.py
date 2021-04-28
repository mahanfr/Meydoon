from django.contrib.auth.decorators import login_required 
from django.shortcuts import redirect, render
from .forms import UserEditForm, UserRegisterForm, ProfileEditForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
       form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'u_form': user_form,
        'p_form': profile_form
    }

    return render(request, 'users/profile_edit.html', context)
    
@login_required
def profile(request):
    return render(request,'users/profile.html')