from django.urls import path
import django.contrib.auth.views as auth_view
from django.views.generic.base import TemplateView
from accounts.views import UserCreationView

urlpatterns=[
    path('login/',auth_view.LoginView.as_view(),name='login'),
    #path('logout/',auth_view.LogoutView.as_view(),name='logout'),
    #path("logout/", TemplateView.as_view(template_name="logout.html"), name="logout"),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('signup/',UserCreationView.as_view(),name='sign_up'),
    path('password_change/',auth_view.PasswordChangeView.as_view(),name='password_change'),
    path('password_change_done/',auth_view.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/',auth_view.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done/',auth_view.PasswordResetDoneView.as_view(),name='password_reset_done')
]