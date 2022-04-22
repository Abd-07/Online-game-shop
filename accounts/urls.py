from django.urls import path
import django.contrib.auth.views as auth_view

urlpatterns=[
    path('login/',auth_view.LoginView.as_view(),name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
]