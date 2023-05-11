from django.urls import path
from .views import imageHome


urlpatterns = [
    path("",imageHome,name='imageHome'),
]