from django.shortcuts import render

from .models import ImageEnhance

# Create your views here.
def imageHome(request):
    images = ImageEnhance.objects.all()
    
        
    return render(request,'image_home.html',{'images':images})
