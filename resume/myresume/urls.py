from django.urls import path
from . import views



urlpatterns = [
    path('',views.portfolio,name='portfolio'),
    path('ideamagix/',views.idea,name='ideamagix'),
    path('watch/',views.watch,name='watch'),


]
