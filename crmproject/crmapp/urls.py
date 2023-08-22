from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path('register/', views.register, name="register"),
    path('my_login/', views.my_login, name="my_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    # create CRUD
    path('create_record/', views.create_record, name="create_record"),
    path('update-record/<int:pk>', views.update_record, name='update-record'),
    path('record/<int:pk>', views.singular_record, name="record"),
    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),
]