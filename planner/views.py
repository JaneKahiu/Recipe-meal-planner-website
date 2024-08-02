from django.shortcuts import render, redirect 
from .models import Recipe
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.urls import reverse
 
# Create your views here.
# create a recipe page

def recipe(request):
    if request.method == 'POST':
        data = request.POST
        day = data.get('day')
        name = name.get('name')
        description = data.get('description')
        Recipe.objects.create(
            day = day,
            name = name,
            description = description,
        )
        return redirect('/')
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            day__icontains=request.GET.get('search'))

    context = { 'recipes': queryset} 
    return render(request, 'recipe.html', context)   

#update recipe data

def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        day = data.get('day')
        name = data.get('name')
        description = data.get('description')

        queryset.day = day
        queryset.name = name
        queryset.description = description
        queryset.save()
        return redirect('/')
    context = {'recipe': queryset}
    return render(request, 'update_recipe.html', context)


#delete the recipe data
def delete_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/')

#register the page of the user

def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect(reverse('register_page'))
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account created")
            return redirect(reverse('login_page'))
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect(reverse('register_page'))
    return render(request, "register.html")

# logout function
def logout(request):
    logout(request)
    return redirect('/login')

#generate the bill

# views.py

from django.shortcuts import render, redirect
from .models import Recipe

def pdf(request):
    if request.method == 'POST':
        data = request.POST
        day = data.get('day')
        name = data.get('name')
        description = data.get('description')

        Recipe.objects.create(
            day=day,
            name=name,
            description=description,
        )

        return redirect('pdf')
    
    queryset = Recipe.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(
            day__icontains=request.GET.get('search')
        )
    
    context = {'recipes': queryset}
    return render(request, 'pdf.html', context)

#login page

def login_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect(reverse('login_page'))
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                return redirect(reverse('recipe'))
            messages.error(request, "Wrong Password")
            return redirect(reverse('login_page'))
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect(reverse('register_page'))
    return render(request, "login.html")

    