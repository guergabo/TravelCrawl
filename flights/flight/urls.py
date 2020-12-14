from django.urls import path  # path
from .import views            # bring views.import.


app_name = 'flight'           #


### URLS ###
urlpatterns =[
    path('', views.HomeSearchView.as_view(), name='main'),
]