from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.gallery,name='gallery'),
    path('photo/<str:pk>/',views.viewPhoto,name='photo'),
    path('add/',views.addPhoto,name='add'),
    # path('photo-delete/<int:pk>/',views.TaskDelete.as_view(),name='task-delete'),
    path('photo_delete/<photo_id>',views.photoDelete,name='photo-delete'),
    path('catrgory_delete/<cat_id>',views.categoryDelete,name='category-delete'),
    path('update_description/<des_id>',views.update_view,name='update-description'),

    # # path('verify/', views.verify_code,name='verify'),
    # path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    # path('register/',views.registerUser,name='register'),
    path('verify/', views.verify_code,name='verify'),

    path('register/', views.registerUser,name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name='scrap_album/login.html'),name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='scrap_album/logout.html'),name='logout'),
    # path('maintenance/', views.maintenance, name='maintenance'),
]
