from django.shortcuts import render,HttpResponseRedirect
from App_Login.forms import CreateNewUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from App_Login.models import UserProfile
# Create your views here.

def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile=UserProfile(user=user)
            request.session['registered']=registered
            return HttpResponseRedirect(reverse('App_Login:login'))

    context = {'tittle':'sign_up','form': form, 'registered': registered}
    return render(request, 'App_Login/sign_up.html', context)

def login_page(request):
 
    try:
      registered= request.session.get('registered',None)
      del request.session['registered']
    except:
      registered=False

    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #registered=True
                return HttpResponseRedirect(reverse('index'))
    context={'tittle':'login','form':form,'registered':registered}
    return render(request, 'App_Login/login.html',context)