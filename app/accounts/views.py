from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# def login_view(request):
#     """
#     path('login/', views.login_view, name='login'), 를 받아 처리하는 view
#
#     django.contrib.auth 앱을 사용하여 loginview를 대체하여 이 메서드는 사용하지 않음
#     """
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(request, username=username, passwor=password)
#         login(request, user)
#
#         return redirect('accounts:profile')
#     else:
#         return render(request, 'accounts/login.html')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')