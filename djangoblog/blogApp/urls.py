"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path

from blogApp.views import index
from blogApp import views
urlpatterns = [
   
    path('', index, name='index'),
    path('author/<name>',views.getAuthor,name="author"),
    path('article/<int:id>',views.getSingle,name="single_post"),
    path('topic/<name>', views.getTopic,name="topic"),
    path('login', views.getLogin,name="login"),
    path('logout', views.getLogout,name="logout"),
    path('create', views.getCreate,name="create"),
    path('profile', views.getProfile,name="profile"),
    path('update/<int:pid>', views.getUpdate,name="update"),
    path('delete/<int:pid>', views.getDelete,name="delete")
]
