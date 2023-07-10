"""
URL configuration for application project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import db.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('valid_objects/', views.get_valid_for_excel_objects.as_view()),
    path('not_valid_objects/', views.get_not_valid_for_excel_objects.as_view()),
    path('one_item/', views.get_one_item_data.as_view()),
    path('all_items/', views.get_all_items_data.as_view()),
    path('show_image/', views.show_image),
    path('get_excel/', views.get_excel),
    path('add_data', views.add_data),
    path('change_data', views.change_data),
    path('get_all_images/', views.get_all_images),

]
