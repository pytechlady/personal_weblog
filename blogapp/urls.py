from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name = 'logout'),
    path('homepage', views.homepage, name='homepage'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('create_blog', views.create_blog, name = 'create_blog'),
    path('delete_blog/<blog_id>', views.delete_blog, name='delete_blog'),
    path('update_blog/<blog_id>', views.update_blog, name='update_blog'),
    
]