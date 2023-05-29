from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect, render


class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    
# def registerUser(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
        
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
    
#     return render(request, 'register.html', {'form': form})


# def userLogin(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
        
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
    
#     return render(request, 'login.html', {'form': form})