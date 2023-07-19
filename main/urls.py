from django.urls import path
from .views import Index, SendPost

app_name = 'main'

urlpatterns = [
   path('', Index.as_view(), name='index'),
   path('sendpost', SendPost, name='sendpost')
]
