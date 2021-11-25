from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import Blogs
from django.views.generic import UpdateView
from .form import Createform

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email = email, first_name=firstname, last_name=lastname)
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    user.save()
                    return redirect('dashboard')
        else:
            messages.error(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'register.html')
  
@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated:
        blogs = Blogs.objects.order_by('-create_date').filter(user_id=request.user.id)
        data={
            'blogs' : blogs,
        }
        return render(request, 'dashboard.html', data)
    else:
        messages.error(request, "please Login")
        return redirect('login')
    
def homepage(request):
    blogs= Blogs.objects.order_by('-create_date')
    data = {
        'blogs' : blogs,
    }
    return render(request, 'index.html', data)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('homepage')
    return redirect('homepage')
  

def create_blog(request):
    if request.method == 'POST':
        blog_title = request.POST['blog_title']
        description = request.POST['description']
        blog_tag = request.POST['blog_title']
        author= request.user
        if request.user.is_authenticated:
            user_id =request.user.id
            blog = Blogs.objects.create(blog_title=blog_title, description=description, user_id=user_id, blog_tag=blog_tag, author=author)
            messages.success(request, 'Blog Created Successfully')
            blog.save()
            return redirect('dashboard')
    return render(request, 'create_blog.html')

def delete_blog(request, blog_id=None):
    blog = Blogs.objects.get(id=blog_id)
    blog.delete()
    messages.success(request, 'Blog Deleted Successfully')
    return redirect('dashboard')

@login_required(login_url='login')
def update_blog(request, blog_id):
        obj= get_object_or_404(Blogs, id=blog_id)
        
        form = Createform(request.POST or None, instance= obj)
        context= {'form': form}

        if form.is_valid():
                obj= form.save(commit= False)

                messages.success(request, "You successfully updated the blog post")
                obj.save()

                return redirect('dashboard')

        else:
                context= {'form': form,
                           'error': 'The form was not updated successfully. Please enter in a title and content'}
                return render(request,'update_blog.html' , context)
        



