from django.contrib.auth import forms
from django.shortcuts import redirect, render
from .forms import MyForm, UserRegisterForm
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from django.urls import reverse_lazy


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

class EditProfileView(generic.UpdateView):
    form_class = MyForm
    template_name = 'users/editprofile.html'
    success_url = reverse_lazy('editprofile')
    def get_object(self):
        return self.request.user

def profile(request):
    return render(request,'users/profile.html')