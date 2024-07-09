from django.urls import path
from . import views
urlpatterns = [
    path('',views.deshboard,name='deshboard'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contract',views.contract,name='contract'),
    path('blog/',views.blog,name='blog'),
]
