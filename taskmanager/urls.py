"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path, include

#urlpatterns = [
 #   path('admin/', admin.site.urls),
  #  path('accounts/', include('django.contrib.auth.urls')),  # Add auth URLs
   # path('', include('tasks.urls')),  # Add app URLs
#]

#from django.contrib import admin
#from django.urls import path, include
#from django.contrib.auth import views as auth_views
#from django.shortcuts import redirect

#urlpatterns = [
   # path('admin/', admin.site.urls),
   # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Login URL
  #  path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL
   # path('', home, name='home'),  # Redirect to login page
 #   path('', lambda request: redirect('login')),  # Redirect root to login

 #   path('', include('tasks.urls')),  # Includes URLs from your 'tasks' app
#]

from django.contrib import admin  # Import the admin module here
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tasks import views  # Import your tasks views to use them
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),  # Access the admin interface at /admin/
    path('tasks/', include('tasks.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Login page
    #path('accounts/register/', views.register, name='register'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout page
    path('', lambda request: HttpResponseRedirect('/accounts/login/')),  # Redirect root to login
    path('tasks/', views.task_list, name='task_list'),  # Task list page
    path('add/', views.add_task, name='add_task'),  # Add a new task
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # Edit a task
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete a task
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]


