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

            instance.grayscale()
            instance.save()
            #latest_object = ImageEnhance.objects.latest('id')
            #latest_object.grayscale()

            return render(request,"image_process.html",{"form":form,'object':instance,"filter":"Not Processed"})
        else:
            latest_object = ImageEnhance.objects.latest('id')
            process = request.POST["first-dropdown"]
            try:
                sub_process = request.POST["second-dropdown"]
                
            except:
                pass

            try:
                tuning_value = request.POST["num-Input"]
            except:
                pass

            if process == '1':
                print("************Basic Selected")
                print(sub_process)

                if sub_process == '1B':
                    print("********* Bit Plane Slicing Selected")
                    tuning_value = int(tuning_value)
                    latest_object.bitPlane(tuning_value)
                    return render(request,"image_process.html",{"form":form,"object":latest_object})
                
                elif sub_process == "1C":
                    print("********* Power Transform Selected")
                    tuning_value = float(tuning_value)
                    latest_object.powerTransform(tuning_value)
                    return render(request,"image_process.html",{"form":form,"object":latest_object})
                elif sub_process == "1D":
                    print("******************* Image Threshold selected")
                    tuning_value = float(tuning_value)
                    latest_object.thresholdImage(tuning_value)
                    return render(request,"image_process.html",{"form":form,"object":latest_object})
                
                elif sub_process == "1E":
                    print("******************* Negative Image selected")
                    latest_object.negativeImage()
                    return render(request,"image_process.html",{"form":form,"object":latest_object})
                
                elif sub_process == "1F":
                    print("******************* Histogram Equalization selected")
                    latest_object.histogramEqImage()
                    return render(request,"image_process.html",{"form":form,"object":latest_object})



                
                return render(request,"image_process.html",{"form":form,"object":latest_object})
            


            elif process == '2':
                print("************ Spatial Filter Selcted")
                print(sub_process)

                if sub_process == "2B":
                    print("************************Smooth filter selected")
                    tuning_value = int(tuning_value)
                    latest_object.smoothFilter(tuning_value)
                    return render(request,"image_process.html",{"form":form,"object":latest_object})
                
                elif sub_process == "2C":
                    print("************************ Sharp filter selected")
                    tuning_value = int(tuning_value)
                    latest_object.sharpFilter(tuning_value)
                    return render(request,"image_process.html",{"form":form,"object":latest_object})
                
                elif sub_process == '2D':
                    print("************************ Min filter selected")
                    tuning_value = int(tuning_value)
                    latest_object.minFilter(tuning_value)
                    return render(request,"image_process.html",{"form":form,"object":latest_object})
                
                elif sub_process == '2E':
                    print("************************ Max filter selected")
                    tuning_value = int(tuning_value)
                    latest_object.maxFilter(tuning_value)
                    return render(request,"image_process.html",{"form":form,"object":latest_object})
                
                elif sub_process == '2F':
                    print("************************ Median filter selected")
                    tuning_value = int(tuning_value)
                    latest_object.medianFilter(tuning_value)
                    return render(request,"image_process.html",{"form":form,"object":latest_object})
                
                elif sub_process == '2G':
                    print("************************ High boost filter selected")
                    tuning_value = int(tuning_value)
                    latest_object.highBoostFilter(tuning_value)
                    return render(request,"image_process.html",{"form":form,"object":latest_object})
                
                return render(request,"image_process.html",{"form":form,"object":latest_object})
            

            elif process == '3':
                print("************ Freuency Filter Selected")

                if sub_process == "3B":
                    print("*********************Low pass filter selected")
                    latest_object.lowpassFilter()
                    return render(request,"image_process.html",{"form":form,"object":latest_object})
                
                elif sub_process == "3C":
                    print("*********************High pass filter selected")
                    latest_object.highpassFilter()
                    return render(request,"image_process.html",{"form":form,"object":latest_object})

                return render(request,"image_process.html",{"form":form,"object":latest_object})
            
                    
    else:
        form = ImageForm()

    return render(request,"image_form.html",{'form':form})
