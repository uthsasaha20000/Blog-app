from django.shortcuts import render,HttpResponseRedirect
from App_Login.forms import CreateNewUser, EditProfile
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from App_Login.models import UserProfile
from django.contrib.auth.decorators import login_required
from App_Login.models import UserProfile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        #form = CreateNewUser(data=request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2= request.POST.get('password2')
        if password != password2:
            messages.error(request, "Passwords do not match")
            return HttpResponseRedirect(reverse('App_Login:signup'))  # Replace 'signup' with the URL name of your signup page
        user = User.objects.create_user(username=username, email=email, password=password)
        registered = True
        user_profile=UserProfile(user=user)
            
        user_profile.save()
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


    if request.method == 'POST':
        
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Blog:blog_list'))
    context={'registered':registered}
    return render(request, 'App_Login/login.html',context)

@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:edit'))
    return render(request, 'App_Login/profile.html', context={'form':form, 'title':'Edit Profile'})

@login_required
def logout_user(request):
    
    logout(request)
    
      
    return HttpResponseRedirect(reverse('App_Login:login'))