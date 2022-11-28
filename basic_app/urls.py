from django.urls import path 
from basic_app import views 

#  Templates ruls

app_name = 'basic_app'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('profile/',views.user_profile,name='user_profile'),
]
