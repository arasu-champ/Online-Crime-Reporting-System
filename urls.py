from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from accounts import views
urlpatterns=[
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView, name="dashboard"),
    path('ajaxregister',views.dashboardView),
    path('accounts',views.dashboardView),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    
    #path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
]