from django.shortcuts import render
from django.http import HttpResponse
from .models import ImageEnhance
from .forms import ImageForm

# Create your views here.


# Create your views here.
def imageHome(request):
       
    try:
        images = ImageEnhance.objects.all()
        
        return render(request,'image_home.html',{'images':images})
    except:
        return HttpResponse("We do not have any images to show you")
    
def imageForm(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            #save the model instance
            instance = form.save(commit=False)
            
            instance.save()

            return render(request,"image_process.html",{"form":form,'object':instance})
        else:
            latest_object = ImageEnhance.objects.latest('id')
            process = request.POST["first-dropdown"]

            if process == '1':
                print("************Basic Selected")
                return HttpResponse("Basic Selected")

            elif process == '2':
                print("************ Spatial Filter Selcted")
                return HttpResponse("Spatial Filter Selected")
            elif process == '3':
                print("************ Freuency Filter Selected")
                return HttpResponse("Frequency Filter Selected")

        
    else:
        form = ImageForm()

    return render(request,"image_form.html",{'form':form})
