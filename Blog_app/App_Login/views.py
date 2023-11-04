from django.shortcuts import render
from django.contrib.auth import UserCreationForm

# Create your views here.
def sign_up(request):
    form=UserCreationForm()
    if request.method=='POST':
        form