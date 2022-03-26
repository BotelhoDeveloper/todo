from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('list/<int:pk>', views.list, name='list'),
    path('edit/<int:pk>', views.edit, name='edit'),
]
