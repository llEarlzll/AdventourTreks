from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm





#from my_app import views


# Create your views here.

def home(request):
    return render(request, 'mysite/home.html')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']

            fname =  userObj['fname']
            lname =  userObj['lname']
            Gender =  userObj['Gender']
            DOB =  userObj['DOB']
            

            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'mysite/register.html', {'form' : form})

#new add

def index(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return HttpResponseRedirect(reverse('mysite:index'))
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'mysite/index.html', context)




    #newadd

"""
    def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'mysite/index.html', {'form': form})
            else:
                return render(request, 'mysite/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'mysite/login.html', {'error_message': 'Invalid login'})
    return render(request, 'mysite/login.html')
"""


"""
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...

"""



def login_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'mysite/login.html', {'form': form})







