"""
URL configuration for startdjingo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.shortcuts import HttpResponse
from book import views


def index(request):
    return HttpResponse("welcome")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book', views.book_detail_query_string),

    path('book/<int:book_id>', views.book_detail_path),
    path('book/str/<str:book_id>', views.book_str),
    path('book/slug/<slug:book_id>', views.book_slug, name='book_slug'),
    path('book/path/<path:book_id>', views.book_path, name='book_path')
]
