from django.urls import path
from .views import HomeTemplateView
from .views import ideamagix

urlpatterns = [
    path('', HomeTemplateView.as_view()),
    path('ideamagix/',ideamagix,name='ideamagix'),
]
