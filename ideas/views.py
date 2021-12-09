from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from.forms import IdeaForm
from .models import Idea

# Create your views here.

def home(request):
    return render(request, 'ideas/home.html')

def signupuser(request):
    if request.method=='GET':
        return render(request, 'ideas/signupuser.html', {'form':UserCreationForm()})
    else:
        #Create a new user
        if request.POST['password1'] == request.POST['password2']:
            #check if password and confirm password matches
            try:
                #check if username is already exist
                user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('allideas')

            except IntegrityError:
                #if username already exist, through error
                return render(request, 'ideas/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'username already taken'})
        else:
            #if password doesnot match confirm password
            return render(request, 'ideas/signupuser.html', {'form': UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    #Existing user login
    if request.method=='GET':
        #if user has already logged in
        return render(request, 'ideas/loginuser.html', {'form':AuthenticationForm()})
    else:
        #if user is login in, check username and password
        user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            #if password or username dose not match, or is enable to find the user

            return render(request, 'ideas/loginuser.html', {'form': AuthenticationForm(), 'error':'User name or password does not match'})
        else:
            #if username and password are correct
            login(request, user)
            return redirect('allideas')


def logoutuser(request):
    #logout fnction
    if request.method == 'POST':
        logout(request)
        return redirect('home') #redirecting to home page

def createidea(request):
    #idea submition form

    if request.method == 'GET':
        return render(request, 'ideas/createidea.html', {'form':IdeaForm()})#for this, we will make a new python file called forms.py in the app i.e. ideas
    else:
        #Creating an idea
        try:
            form = IdeaForm(request.POST)
            newidea = form.save(commit=False)#This will privent saving in the data base
            newidea.user = request.user #To enable user to edit and create only his idea and privent other users from editing his idea
            newidea.save()
        except ValueError:
            return render(request, 'ideas/createidea.html', {
                'form': IdeaForm(), 'error':'word limit exceeded!!'})  # for this, we will make a new python file called forms.py in the app i.e. ideas

        return redirect('allideas')
def allideas(request):
    ideas= Idea.objects.filter(user=request.user) #get ideas of the user logged in
    return render(request, 'ideas/ideas.html', {'ideas':ideas}) #request ideas and display on the ideas.html

def viewidea(request, idea_pk):
    idea = get_object_or_404(Idea, pk=idea_pk, user=request.user) #get the ID of the idea
    if request.method == 'GET':
        form = IdeaForm(instance=idea)
        return render(request, 'ideas/viewidea.html', {'idea': idea, 'form':form})
    else:
        try:
            form = IdeaForm(request.POST, instance=idea)
            form.save()
            return redirect('allideas')
        except ValueError:
            return render(request, 'ideas/viewidea.html', {'idea': idea, 'form':form, 'error': 'Bad info'})

def deleteidea(request, idea_pk):
    idea = get_object_or_404(Idea, pk=idea_pk, user=request.user)  # deleting the idea form database
    if request.method == 'POST':
        idea.delete()
        return redirect('allideas')

