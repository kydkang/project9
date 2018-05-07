from django.urls import path
from django.conf.urls import url
from rango import views 

urlpatterns = [
    path('', views.index, name='index'), 
    path('about/', views.about, name='about'), 
    path('add_category/', views.add_category, name='add_category'), 
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category,name='show_category'),
    path('category/<slug:category_name_slug>/',views.show_category,name='show_category'), 
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    path('category/<slug:category_name_slug>/add_page/',views.add_page, name='add_page'), 
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'), 
    # path('logout/', views.user_logout, name='logout'), 
    path('restricted/', views.restricted, name='restricted'),
    path('goto/', views.track_url, name='goto'), 
    path('register_profiles/', views.register_profile, name='register_profile'),
    path('profile/str:<username>/', views.profile, name='profile'), 
    path('profiles/', views.list_profiles, name='list_profiles'), 

     
]
