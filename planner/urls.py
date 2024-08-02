from django.urls import path
from  . import views

urlpatterns = [
    path('', views.recipe, name='recipe'),
    path('update_recipe/<int:id>/', views.update_recipe, name='update_recipe'),
    path('delete_recipe/<int:id>/', views.delete_recipe, name='delete_recipe'),
    path('register_page/', views.register_page, name='register_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout/', views.logout, name='logout'),
    path('pdf/', views.pdf, name='pdf'),
]