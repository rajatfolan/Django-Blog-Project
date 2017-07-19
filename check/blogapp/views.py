
from django.shortcuts import render
from django.http import *
from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib import auth
# Create your views here.

def index(request):
    return render(request,'loggedin.html',{'fullname':request.user.username,'pro':request.user.profile})

def home(request):
    if request.user.is_authenticated():
        return index(request)
    else:
        return login(request)



def login(request):
    return render(request,'login.html')


def auth_view(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user=auth.authenticate(username=username,password=password)


	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    if request.user.is_authenticated():
        return render(request,'loggedin.html',{'fullname':request.user,'pro':request.user.profile})
    else:
        return HttpResponseRedirect('/')


def invalid_login(request):
    return render(request,'invalid.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #form=RegisterForm(request.POST)
        #print form['username']
        if form.is_valid():
            form.save()
            return HttpResponse('Registered')

    else:
        form = UserCreationForm()
        return render(request,'register.html',{'form':form})


def blog_post(request):
    objs=Blog.objects.all()
    num_visit = request.session.get('num_visit' , 1)
    request.session['num_visit'] = num_visit+1



    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.user=request.user
            blog.save()

    else:
        form=BlogForm()

    return render(request,'blog.html',{'form':form,'fullname':request.user.username,'objs':objs,'pro':request.user.profile,'nv':num_visit})

def delete(request,id):
    obj=Blog.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/accounts/loggedin/blogs/')

def edit(request,id):
    n=Blog.objects.get(id=id)
    if request.method=='POST':
        form=BlogForm(request.POST,instance=n)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/loggedin/blogs/')

    else:
        form=BlogForm(instance=n)
    return render(request,'editblog.html',{'form':form})



def detail(request):
    if request.method == 'POST':
        form = DetailForm(request.POST,instance=request.user)
        proform = ProfileForm(request.POST,instance=request.user.profile)
        if form.is_valid() and proform.is_valid():
            form.save()
            proform.save()
            pro = Profile.objects.get(user = request.user.profile.user)
            #return render(request,'detail.html',{'form':form,'proform':proform,'pro':pro})
            #return HttpResponseRedirect('/accounts/loggedin/')

    else:
        form = DetailForm(instance = request.user)
        proform = ProfileForm(instance = request.user.profile)
        pro = Profile.objects.get(user = request.user.profile.user)
    return render(request,'detail.html',{'form':form,'proform':proform,'pro':pro,'fullname':request.user.username})






def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login/')
            #return render(request,'detail.html',{'form':form,'proform':proform,'pro':pro})
            #return HttpResponseRedirect('/accounts/loggedin/')

    else:
        form = PasswordChangeForm(user = request.user)
    return render(request,'passwordChange.html',{'form':form,'fullname':request.user.username})
