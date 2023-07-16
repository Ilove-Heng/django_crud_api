"""django_api_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from .views import index,detail,TaskApiView,TaskDetailApiView,TaskViewSet,myuserviewset,LoginApi
from rest_framework.routers import DefaultRouter 


router = DefaultRouter()
# model view set
router.register('viewsets',TaskViewSet,basename='viewset')
router.register('auths',myuserviewset,basename='auth')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/task',index),
    path('api/task/<int:id>',detail),
    path("apiview/task",TaskApiView.as_view()),
    path("apiview/task/<int:id>",TaskDetailApiView.as_view()),
    path('login/',LoginApi.as_view()),
    path('',include(router.urls))
]


# example
# ! http://127.0.0.1:8000/viewsets/8/