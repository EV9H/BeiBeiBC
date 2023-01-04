from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from . import db_helper
# Database
db = db_helper.db

# Create your views here.
def index(request):
    return render(request, "beiciApp/index.html")

def users(request):
    user_list = db.user.find()
    context = {
        'users' : user_list
    }

    return render(request, "beiciApp/users.html", context )

def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'beiciApp/signup.html', {'form': form})

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('passsword')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            request.session["username"]=user.username
            request.session["is_authorized"]=True
            request.session["is_superuser"]=user.is_superuser
            request.session["is_staff"]=user.is_staff
            # response = HttpResponseRedirect('/home/?redirect_to='+str(redirect_to), {
            #     "username":request.session["username"]
            # })
            # return response
            return HttpResponseRedirect('/index')
        else:
            return render(request, 'beiciApp/users.html')
    else:
        return render(request, 'beiciApp/users.html')