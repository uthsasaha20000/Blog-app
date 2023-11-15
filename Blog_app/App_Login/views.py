from django.shortcuts import render,HttpResponseRedirect
from App_Login.forms import CreateNewUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
# Create your views here.

def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            pass

    context = {'tittle':'sign_up','form': form, 'registered': registered}
    return render(request, 'App_Login/sign_up.html', context)

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'App_Login/login.html', context={'form':form})