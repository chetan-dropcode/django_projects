from django.urls import path
from .views import HomeTemplateView
from .views import ideamagix,watch

urlpatterns = [
    path('', HomeTemplateView.as_view()),
    path('ideamagix/',ideamagix,name='ideamagix'),
    path('watch/',watch,name='watch'),

]
