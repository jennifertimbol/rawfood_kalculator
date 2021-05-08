from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('createaccount', views.createaccount),
    path('signin', views.signin),
    path('profile', views.userprofile),
    path('rawfoodkalculator/petinfo', views.petinfo),
    path('rawfoodkalculator/addpetinfo', views.addpetinfo),
    path('rawfoodkalculator/addpet', views.addpet),
    path('rawfoodkalculator/results', views.results),
    path('logout', views.logout),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)