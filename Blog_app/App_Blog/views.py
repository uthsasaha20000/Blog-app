from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from App_Login.models import UserProfile
# Create your views here.
@login_required
def blog_list(request):
  if request.method=='GET':
   search=request.GET.get('search','')
   result=User.objects.filter(username__icontains=search)

   return render(request,'App_Blog/blog_list.html',context={'search':search,'result':result})