"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from vendor import views #之前一直出現views未定義 網路答案: https://stackoverflow.com/questions/24650261/django-nameerror-name-views-is-not-defined

urlpatterns = [
	# path('', views.showtemplate), 原來的寫法 d15改成以下
	path('', views.vendor_index, name="vendor_index"),
	path('create', views.vendor_create_view), #d18新增
]
