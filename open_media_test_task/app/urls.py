from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('page/create', views.create_page, name='create_page'),
    path('page/<uuid:uid>', views.view_page_object, name='view_page_object'),
    path('page/list', views.list_page_objects, name='list_page_objects'),
]