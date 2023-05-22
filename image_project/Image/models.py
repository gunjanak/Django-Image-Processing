
from django.db import models
from django.core.files import File

from io import BytesIO

from PIL import ImageFilter
from PIL import Image


from . import basic
from . import spatial
from . import frequency


def grayScale(image):
    img = Image.open(image).convert('L')
    img = img.resize((400,400))
    img_out = img


    in_io = BytesIO()
    img.save(in_io,'PNG',quality=85)
    img = File(in_io,name=image.name)

    out_io = BytesIO()
    img_out.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=image.name)


    return [img,out_final]

    
def imageRotate(image,deg=90):
    im = Image.open(image).convert('L')
   
    out = im.rotate(deg)
    out_io = BytesIO()
    out.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=image.name)
    return out_final


def imageTranspose(image):
    im = Image.open(image).convert('L')
   
    out = im.transpose(Image.FLIP_LEFT_RIGHT)
    out_io = BytesIO()
    out.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=image.name)
    return out_final


# Create your models here.
class ImageEnhance(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="",blank=True,null=True)
    image_enhanced = models.ImageField(upload_to="",blank=True,null=True)
    filter = models.CharField(max_length=50,blank=True,null=True)
    likes = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    

    def grayscale(self,*args,**kwargs):
        self.image,self.image_enhanced = grayScale(self.image)
        super().save(*args,**kwargs)


    def rotateMe(self,deg=90,*args,**kwargs):
        self.image_enhanced = imageRotate(self.image,deg)
        super().save(*args,**kwargs)

    def transposeMe(self,*args,**kwargs):
        self.image_enhanced = imageTranspose(self.image)
        super().save(*args,**kwargs)

    #Handling basic operations
    def bitPlane(self,bit=3,*args,**kwargs):
        
        self.image,self.image_enhanced = basic.Bit_Plane(self.image,bit)
        self.filter = "Bit Slice"
        super().save(*args,**kwargs)

    def powerTransform(self,gamma=2,*args,**kwargs):
        self.image,self.image_enhanced = basic.Power_transform(self.image,gamma)
        self.filter = "Power Transform"
        super().save(*args,**kwargs)

    def thresholdImage(self,threshold=150,*args,**kwargs):
        self.image,self.image_enhanced = basic.Threshold(self.image,threshold)
        self.filter = "Threshold Image"
        super().save(*args,**kwargs)

    def negativeImage(self,*args,**kwargs):
        self.image,self.image_enhanced = basic.Negative(self.image)
        self.filter = "Negative Image"
        super().save(*args,**kwargs)

    def histogramEqImage(self,*args,**kwargs):
        self.image,self.image_enhanced = basic.Histogram_equalization(self.image)
        self.filter = "Histogram Equalized"
        super().save(*args,**kwargs)

    #methods for spatial filters
    def smoothFilter(self,kernel_size=3,*args,**kwargs):
    
        self.image,self.image_enhanced = spatial.Smooth_Filter(self.image,kernel_size)
        self.filter = "Smooth Filter"
        super().save(*args,**kwargs)

    def sharpFilter(self,kernel_size=3,*args,**kwargs):
        self.image,self.image_enhanced,_ = spatial.Sharp_Filter(self.image,kernel_size)
        self.filter = "Sharp Filter"
        super().save(*args,**kwargs)

    def minFilter(self,kernel_size=3,*args,**kwargs):
        self.image,self.image_enhanced = spatial.Min_Filter(self.image,kernel_size)
        self.filter = "Min Filter"
        super().save(*args,**kwargs)

    def maxFilter(self,kernel_size=3,*args,**kwargs):
        self.image,self.image_enhanced = spatial.Max_Filter(self.image,kernel_size)
        self.filter = "Max Filter"
        super().save(*args,**kwargs)

    def medianFilter(self,kernel_size=3,*args,**kwargs):
        self.image,self.image_enhanced = spatial.Median_Filter(self.image,kernel_size)
        self.filter = "Median Filter"
        super().save(*args,**kwargs)

    def highBoostFilter(self,kernel_size=3,*args,**kwargs):
        self.image,self.image_enhanced = spatial.High_Boost(self.image,kernel_size)
        self.filter = "High Boost"
        super().save(*args,**kwargs)

    #Frequency filters
    def lowpassFilter(self,*args,**kwargs):
        self.image,self.image_enhanced,_ = frequency.low_pass_filter(self.image)
        self.filter = "Low Pass Filter"
        super().save(*args,**kwargs)

    def highpassFilter(self,*args,**kwargs):
        self.image,self.image_enhanced = frequency.high_pass_filter(self.image)
        self.filter = "High Pass Filter"
        super().save(*args,**kwargs)




    




    def __str__(self):
        return self.title