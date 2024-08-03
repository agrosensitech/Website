from django.urls import path 
from . import views  

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('gallery/',views.gallery,name="gallery"),
    path('details/<int:id>',views.details,name="details"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('weather/',views.weather,name="weather"),  
    path('login/',views.login_user,name="login"),  
    path('logout/',views.logout_user,name="logout"),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)