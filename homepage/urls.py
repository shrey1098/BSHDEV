from django.urls import path
from . import views
from django.conf.urls import url

app_name = "homepage"
urlpatterns = [
    path('', views.homepage, name='Homepage'),
    path('our_goal', views.our_goal, name='Our_Goal'),
    path('our_inspiration', views.our_inspiration, name='Our_Inspiration'),
    path('what_do_we_do', views.what_do_we_do, name='What_do_we_do'),
    path('who_we_are', views.who_we_are, name='Who_we_are'),
    path('registration', views.register, name='Register'),

]
