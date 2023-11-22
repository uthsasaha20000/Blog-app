from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def blog_list(request):
    return render(request,'App_Blog/blog_list.html',context={})