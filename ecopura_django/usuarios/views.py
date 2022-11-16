from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, get_user_model

# Create your views here.
class RegistroSesion(View,UserCreationForm):
    
    def get(self,request):
        class Meta:
            model = get_user_model
        return render(request,'registro.html',{'form':form})
    def post(self,request):
        form = UserCreationForm(request.POST)
        usuario  = form.save()
        login(request,usuario)
        return redirect('inicio_url')
