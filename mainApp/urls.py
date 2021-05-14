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
    path('addnewpet', views.addpetinfo),
    path('rawfoodkalculator/results/<int:pet_id>', views.results),
    path('rawfoodkalculator/<int:pet_id>/delete', views.deletepet),
    path('rawfoodkalculator/<int:pet_id>/updatepet', views.updatepet),
    path('update/<int:pet_id>', views.update),
    path('logout', views.logout),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)