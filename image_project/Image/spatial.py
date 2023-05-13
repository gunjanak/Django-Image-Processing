from django.core.files import File

import numpy as np
from PIL import Image
from PIL import ImageFilter
from io import BytesIO

def Smooth_Filter(input_image,kernel_size = 3):
    img = Image.open(input_image).convert('L')
    img = img.resize((400,400))

    # convert to numpy array 
    numpy_image = np.array(img)

    #array for padding
      #array for padding
    x = 400+(kernel_size-1)
    y = 400+(kernel_size-1)
    array_b = np.zeros((x,y))
    

    #to pad initial array with zeros
    array_b[1:401,1:401] = numpy_image

    #defining filter
     #defining filter
    filter_array = np.full((kernel_size, kernel_size), 1/9)

    #creating an empty list
    lst = []
    for i in range(400):
        for j in range(400):
            #extracting part of array equal to filter size
            array_c = array_b[i:(kernel_size+i),j:(kernel_size+j)]
            
            #applying filter
            array_mul = np.multiply(filter_array,array_c)
            array_sum = np.sum(array_mul)
            
            # putting calculated value in list
            lst.append(array_sum)

    #resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image = final_image.convert("L")


    out_io = BytesIO()
    final_image.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=input_image.name)

    in_io = BytesIO()
    img.save(in_io,'PNG',quality=85)
    img = File(in_io,name=input_image.name)

    return [img,out_final]
  

def Sharp_Filter(input_image,kernel_size=3):
    img = Image.open(input_image).convert('L')
    img = img.resize((400,400))

    # convert to numpy array 
    numpy_image = np.array(img)

    #array for padding
    x = 400+(kernel_size-1)
    y = 400+(kernel_size-1)
    array_b = np.zeros((x,y))
    

    #to pad initial array with zeros
    array_b[1:401,1:401] = numpy_image

    denominator = (kernel_size*kernel_size)
    filter_array = np.full((kernel_size, kernel_size), -1/denominator)
    center = int((kernel_size-1)/2)
    filter_array[center,center] = (denominator-1)/denominator
   


    #creating an empty list
    lst = []
    for i in range(400):
        for j in range(400):
            #extracting part of array equal to filter size
            array_c = array_b[i:(kernel_size+i),j:(kernel_size+j)]
            
            #applying filter
            array_mul = np.multiply(filter_array,array_c)
            array_sum = np.sum(array_mul)
            
            # putting calculated value in list
            lst.append(array_sum)

    #resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image = final_image.convert("L")

    out_io = BytesIO()
    final_image.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=input_image.name)

    in_io = BytesIO()
    img.save(in_io,'PNG',quality=85)
    img = File(in_io,name=input_image.name)

    return [img,out_final,final_image]



def Min_Filter(input_image,kernel_size=3):
    

    img = Image.open(input_image).convert('L')
    img = img.resize((400,400))


    # convert to numpy array 
    numpy_image = np.array(img)

    #array for padding
    x = 400+(kernel_size-1)
    y = 400+(kernel_size-1)
    array_b = np.zeros((x,y))
    

    #to pad initial array with zeros
    array_b[1:401,1:401] = numpy_image

  

    #defining filter
    
    filter_array = np.full((kernel_size, kernel_size), kernel_size)

    #creating an empty list
    lst = []
    for i in range(400):
        for j in range(400):
            #extracting part of array equal to filter size
            array_c = array_b[i:(kernel_size+i),j:(kernel_size+j)]
            
            #applying filter
            array_mul = np.multiply(filter_array,array_c)
            array_sum = np.min(array_mul)
            
            # putting calculated value in list
            lst.append(array_sum)

    #resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image = final_image.convert("L")


    out_io = BytesIO()
    final_image.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=input_image.name)

    in_io = BytesIO()
    img.save(in_io,'PNG',quality=85)
    img = File(in_io,name=input_image.name)

    return [img,out_final]


def Max_Filter(input_image,kernel_size=3):
    img = Image.open(input_image).convert('L')
    img = img.resize((400,400))
    # convert to numpy array 
    numpy_image = np.array(img)

    #array for padding
    #array for padding
    x = 400+(kernel_size-1)
    y = 400+(kernel_size-1)
    array_b = np.zeros((x,y))
    

    #to pad initial array with zeros
    array_b[1:401,1:401] = numpy_image

  

    #defining filter
    
    filter_array = np.full((kernel_size, kernel_size), kernel_size)

    #creating an empty list
    lst = []
    for i in range(400):
        for j in range(400):
            #extracting part of array equal to filter size
            array_c = array_b[i:(kernel_size+i),j:(kernel_size+j)]
            
            #applying filter
            array_mul = np.multiply(filter_array,array_c)
            array_sum = np.max(array_mul)
            
            # putting calculated value in list
            lst.append(array_sum)

    #resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image = final_image.convert("L")


    out_io = BytesIO()
    final_image.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=input_image.name)

    in_io = BytesIO()
    img.save(in_io,'PNG',quality=85)
    img = File(in_io,name=input_image.name)

    return [img,out_final]


def Median_Filter(input_image,kernel_size=3):
    

    img = Image.open(input_image).convert('L')
    img = img.resize((400,400))
    # convert to numpy array 
    numpy_image = np.array(img)

    #array for padding
    x = 400+(kernel_size-1)
    y = 400+(kernel_size-1)
    array_b = np.zeros((x,y))
    

    #to pad initial array with zeros
    array_b[1:401,1:401] = numpy_image

  

    #defining filter
    
    filter_array = np.full((kernel_size, kernel_size), kernel_size)

    #creating an empty list
    lst = []
    for i in range(400):
        for j in range(400):
            #extracting part of array equal to filter size
            array_c = array_b[i:(kernel_size+i),j:(kernel_size+j)]
            
            #applying filter
            array_mul = np.multiply(filter_array,array_c)
            array_sum = np.median(array_mul)
            
            # putting calculated value in list
            lst.append(array_sum)

    #resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image = final_image.convert("L")


    out_io = BytesIO()
    final_image.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=input_image.name)

    in_io = BytesIO()
    img.save(in_io,'PNG',quality=85)
    img = File(in_io,name=input_image.name)

    return [img,out_final]



def High_Boost(input_image,kernel_size=3):
    high_pass = Sharp_Filter(input_image,kernel_size)
    high_pass = high_pass[2]

    img = Image.open(input_image).convert('L')
    img = img.resize((400,400))

   
    # convert to numpy array 
    numpy_image = np.array(img)

    A = 3
    high_boost = (A-1)*numpy_image + high_pass
    final_image = Image.fromarray(high_boost)
    final_image= final_image.convert("L")


    out_io = BytesIO()
    final_image.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=input_image.name)

    in_io = BytesIO()
    img.save(in_io,'PNG',quality=85)
    img = File(in_io,name=input_image.name)

    return [img,out_final]