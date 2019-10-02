"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from .views import (home_page, heroes_page, game_page)
from heroCreator.views import (
hero_detail_create_view,
hero_detail_page,
hero_detail_list_view,
hero_detail_update_view,
hero_detail_delete_view,

)



urlpatterns = [
	path('', home_page),
    path('all-heroes/', hero_detail_list_view),
    path('all-heroes-new/', hero_detail_create_view),

    path('heroes/<str:slug>/', hero_detail_page),
    path('heroes/<str:slug>/edit/', hero_detail_update_view),
    path('heroes/<str:slug>/delete/', hero_detail_delete_view),
	path('heroes/', heroes_page),
	path('game/', game_page),
    path('admin/', admin.site.urls),
    path('heroViewer/<int:hero_id>/', hero_detail_page),
]
