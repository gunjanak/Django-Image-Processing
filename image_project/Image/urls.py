from django.urls import path
from .views import imageHome, imageForm


urlpatterns = [
    path("",imageHome,name='imageHome'),
    path("upload/",imageForm,name="imageform"),
]