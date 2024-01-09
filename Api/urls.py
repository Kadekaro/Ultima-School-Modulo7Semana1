from django.urls import path
from Api.views import hello_world

app_name = 'api'
urlpatterns = [
    path('hello_world', hello_world, name='hello_world_api'),
]