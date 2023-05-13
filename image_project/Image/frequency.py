from django.core.files import File

import numpy as np
from PIL import Image,ImageDraw
from PIL import ImageFilter
from io import BytesIO
from scipy import fftpack


def low_pass_filter(input_image):
    
    img = Image.open(input_image).convert('L')
    img = img.resize((400,400))

    #convert image to numpy array
    image1_np=np.array(img)
    #fft of image
    fft1 = fftpack.fftshift(fftpack.fft2(image1_np))
    #Create a low pass filter image
    x,y = image1_np.shape[0],image1_np.shape[1]

    #defining filter
    #size of circle
    e_x,e_y=50,50
    #create a box 
    bbox=((x/2)-(e_x/2),(y/2)-(e_y/2),(x/2)+(e_x/2),(y/2)+(e_y/2))
    low_pass=Image.new("L",(image1_np.shape[0],image1_np.shape[1]),color=0)
    draw1=ImageDraw.Draw(low_pass)
    draw1.ellipse(bbox, fill=1)
    low_pass_np=np.array(low_pass)
    low_pass_np = low_pass_np.T
    #end of defining filter

    #multiply both the images
    filtered=np.multiply(fft1,low_pass_np)

    #inverse fft
    ifft2 = np.real(fftpack.ifft2(fftpack.ifftshift(filtered)))
    ifft2 = np.maximum(0, np.minimum(ifft2, 255))
    data = Image.fromarray(ifft2)  
    low_pass_array = data
    data = data.convert("L") 
    final_image = data

    out_io = BytesIO()
    final_image.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=input_image.name)

    in_io = BytesIO()
    img.save(in_io,'PNG',quality=85)
    img = File(in_io,name=input_image.name)

    return [img,out_final,low_pass_array]
  

def high_pass_filter(input_image):
    img = Image.open(input_image).convert('L')
    img = img.resize((400,400))


    #converting image to array
    image_array = np.array(img)

    #sending image to low pass filter
    
    lowpass_image_array = low_pass_filter(input_image)[2]
    
   
    #subtracting lowpass image from original to obtain highpass image
    high_pass_array = image_array - lowpass_image_array
    print(high_pass_array.shape)

    #array to image
    high_pass_image = Image.fromarray(high_pass_array)  
    high_pass_image = high_pass_image.convert("L")

    final_image = high_pass_image

    out_io = BytesIO()
    final_image.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=input_image.name)

    in_io = BytesIO()
    img.save(in_io,'PNG',quality=85)
    img = File(in_io,name=input_image.name)

    return [img,out_final]



    
    
