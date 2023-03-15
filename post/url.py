from django.urls import path
from . import views

urlpatterns = {
    path('hello/', views.hello, name='hello'),
    path('greet/', views.greet, name='greet'),
    path('locked/', views.locked, name='locked'),
    path('login/', views.login, name='solute')
}
