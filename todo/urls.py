"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import tasks.views
import tasks.api_views

urlpatterns = [
    path('api/tasks/', tasks.api_views.TaskList.as_view(), name="list"),
    path('api/create/', tasks.api_views.TaskCreate.as_view(), name="create"),
    path('api/update/<int:id>/', tasks.api_views.TaskRetrieveUpdateDestroy.as_view(), name="update_delete"),
    

    path('admin/', admin.site.urls),

    path('', tasks.views.index ,name="index"),
    path('update_task/<int:pk>/', tasks.views.updateTask, name="update"),
    path('delete/<int:pk>/', tasks.views.deleteTask, name="delete"),
]   
