from django.urls import path


from .views import (
hero_detail_list_view,
hero_detail_update_view,
hero_detail_delete_view,
hero_detail_retrieve_view,
)

urlpatterns = [
    path('', hero_detail_list_view),
    path('<str:slug>/', hero_detail_retrieve_view),
    path('<str:slug>/edit/', hero_detail_update_view),
    path('<str:slug>/delete/', hero_detail_delete_view),

]
