from django.urls import path
from django.contrib import admin
from mycontacts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show),
    path('add/', views.add),
]