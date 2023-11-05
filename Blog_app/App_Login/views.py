from django.shortcuts import render
#from django.contrib.auth import UserCreationForm

# Create your views here.
def sign_up(request):
    form=UserCreationForm()
    registered=False
    if request.method=='POST':
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registerd=True
    dict={'form':form,'registered':registerd}
    return render(request,'App_Login/sign_up.html',context=dict)