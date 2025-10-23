from django.shortcuts import render,redirect
from .models import Post,Form
from .forms import Contactform,Postform, updateform,Regform,Loginform
# from .postform import Postform,updateform
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login,logout
# from .regform import Regform
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    if request.method =="POST":
        forms = Contactform(request.POST)
        if forms.is_valid():
            forms.save()
    else:
        forms = Contactform()
    return render(request,'home.html',{"forms":forms})


def service(request):
    blogs=Post.objects.all().order_by('-id')
    return render(request, 'service.html',{"blogs":blogs})


def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method =="POST":
        forms = Contactform(request.POST)
        if forms.is_valid():
            forms.save()
    else:
        forms = Contactform()
    return render(request,'contact.html',{"forms":forms})

def singlepage(request,pk):
    post=get_object_or_404(Post,pk=pk)
    context={"post":post}
    return render(request,'singlepage.html',context)

login_required(login_url='login')
def postservice(request):
    forms = Postform()
    if request.method =="POST":
        forms = Postform(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('service')
    else:
        forms = Postform()
    return render(request,'postservice.html',{'forms':forms})

def registration(request):
    if request.method=='POST':
        form=Regform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
       form = Regform()
    return render(request,'registration/registration.html',{'form':form})


login_required(login_url='login')
def dashboard(request):
    post=Post.objects.all()
    return render(request,'dashboard.html',{'post':post})


def delete_post(request,ig):
    post=Post.objects.get(pk=ig)
    post.delete()
    return redirect('dashboard')


def update(request,ig):
   post=Post.objects.get(pk=ig)
   form = updateform(instance=post)
   if request.method=='POST':
       form=updateform(request.POST,instance=post)
       if form.is_valid():
           form.save()
           return redirect('dashboard')
   return render(request,'update.html',{'form':form})


def login(request):
    form=Loginform()
    if request.method == "POST":
        form=Loginform(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user= authenticate(request, username=username,password=password)
            if user is not None:
                auth.login(request,user)
                # messages.success(request, 'You have logged in successfully')
                return redirect('dashboard')
    return render(request,'login.html',{'form':form})

def logout(request):
    auth.logout(request)
    return redirect('login')

login_required(login_url='login')
def admindashboard(request):
    return render(request,'admindashboard.html')

login_required(login_url='login')
def admincontact(request):
    contact=Form.objects.all()
    return render(request,'admincontact.html',{'contact':contact})

