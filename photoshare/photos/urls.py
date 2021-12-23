from django.urls import path
from . import views

urlpatterns = [
    path('',views.gallery,name='gallery'),
    path('photo/<str:pk>/',views.viewPhoto,name='photo'),
    path('add/',views.addPhoto,name='add'),
    # path('photo-delete/<int:pk>/',views.TaskDelete.as_view(),name='task-delete'),
    path('photo_delete/<photo_id>',views.photoDelete,name='photo-delete'),
    path('catrgory_delete/<cat_id>',views.categoryDelete,name='category-delete'),
    path('update_description/<des_id>',views.update_view,name='update-description'),

    
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerUser,name='register'),


]
