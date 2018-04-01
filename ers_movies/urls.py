"""ers_movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin 
from rest_framework_jwt.views import obtain_jwt_token
from .views import user_info
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/login', obtain_jwt_token, name="api-login"),
    url(r'^api/user_info', user_info, name="api-user-info"),
    url(r'^api/catalog/', include('movies_catalog.api.urls'), name="api-catalog"),
    url(r'^api/rent/movies_rent/', include('movies_rent.api.urls'), name="api-rent"),
]
