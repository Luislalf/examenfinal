from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas),
    url(r'', views.examen_nueva, name='pelicula_nueva'),
    #url(r'^examen/nueva/$', views.examen_nueva, name='pelicula_nueva'),
    ]
