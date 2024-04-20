from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('login',views.login_view, name ='login'),
    path('register',views.register,name = "register"),
    path('logout',views.logout_view, name = "logout"),

    #-----CRUD---------
    path("dashboard",views.dashboard, name = "dashboard"),
    path('create_record',views.create_record, name = "create_record"),
    path('update_record/<int:pk>',views.update_record ,name = "update_record"),
    path('record/<int:pk>', views.singular_record, name= "record"),

]