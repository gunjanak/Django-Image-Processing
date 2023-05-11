from django.shortcuts import render
from django.http import HttpResponse
from .models import ImageEnhance

# Create your views here.


# Create your views here.
def imageHome(request):
       
    try:
        images = ImageEnhance.objects.all()
        
        return render(request,'image_home.html',{'images':images})
    except:
        return HttpResponse("We do not have any images to show you")
    