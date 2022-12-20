from django.urls import path
from main import views


urlpatterns =   [
    path('', views.index),
    path('countries-list/', views.ListCountriesPage, name='country'),
    path('languages/', views.languages, name='language'),
    path('countries-list/<int:id>',views.country),
    path('languages/<id_language>', views.languages_index),
]
