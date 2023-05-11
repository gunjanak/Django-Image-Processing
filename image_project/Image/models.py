
from django.db import models
from django.core.files import File

from io import BytesIO

from PIL import ImageFilter
from PIL import Image

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def rotateMe(self,deg=90,*args,**kwargs):
        self.image_enhanced = imageRotate(self.image,deg)
        super().save(*args,**kwargs)

    def transposeMe(self,*args,**kwargs):
        self.image_enhanced = imageTranspose(self.image)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title