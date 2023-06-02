from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('auth/signin/', views.cadastro, name='cadastro'),
    path('auth/login/', views.login, name='login'),
    path('timeline/<str:email>/', views.timeline, name='timeline'),
    path('config/<str:email>/', views.configuracoes, name='configuracoes'),
    path('newpost/<str:email>/', views.novo_post, name='novo_post'),
    path('logout/', views.logout, name='logout'),
    path('auth/forgotpass/', views.esqueci_senha, name='esqueci_senha'),
]