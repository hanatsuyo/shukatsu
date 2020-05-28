from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='main_page'


urlpatterns = [
    path('index', views.index, name='index'),
    path('', auth_views.LoginView.as_view(template_name='main_page/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('company/new', views.company, name='company_new'),
    path('company_detail/<int:pk>', views.company_detail, name='company_detail'),
    path('company/<int:pk>/edit/', views.company_edit, name='company_edit'),
    path("company/<int:pk>/delete/",views.company_delete,name="company_delete"),
    path("company/<int:pk>/delete_comfirm/",views.delete_comfirm,name="delete_comfirm"),


]