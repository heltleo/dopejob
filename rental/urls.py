from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='cars'),
    path('<int:id>/', views.detail, name='car-details'),
    path('contact', views.contact, name='contact'),
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, name='logout'),
    path('pricing', views.PricingView.as_view(), name='pricing'),
]
