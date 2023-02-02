from django.urls import path
from houseapp.views import ShowNodemcusList, ShowNodemcu

app_name = 'houseapp'
urlpatterns = [
    path('', ShowNodemcusList.as_view(), name='house'),
    path('nodes/<int:pk>/', ShowNodemcu.as_view(), name='node_detail'),
]
