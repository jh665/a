from django.urls import path
from . import views

urlpatterns = [
    # path('', views.SingleLanding.as_view()),
    path('about_me/', views.SingleAbout.as_view()),
    path('', views.SingleHome.as_view()),
    path('home/', views.SingleHome.as_view()),
]