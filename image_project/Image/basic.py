

from django.core.files import File

import numpy as np
from PIL import Image
from PIL import ImageFilter
from io import BytesIO



def Bit_Plane(input_image,bit=7):

    img = Image.open(input_image).convert('L')
    img = img.resize((400,400))
    
    numpy_image = np.array(img)
    #Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
    lst = []
    for i in range(numpy_image.shape[0]):
        for j in range(numpy_image.shape[1]):
            lst.append(np.binary_repr(numpy_image[i][j] ,width=8)) # width = no. of bits

    value = (pow(2,(bit-1)))
    
    # We have a list of strings where each string represents binary pixel value. To extract bit planes we need to iterate over the strings and store the characters corresponding to bit planes into lists.
    # # Multiply with 2^(n-1) and reshape to reconstruct the bit image.
    eight_bit_img = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * value).reshape(400,400)
    bit_sliced_image = Image.fromarray(eight_bit_img)

    final_image = bit_sliced_image .convert("L")

    out_io = BytesIO()
    final_image.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=input_image.name)

    in_io = BytesIO()
    img.save(in_io,'PNG',quality=85)
    img = File(in_io,name=input_image.name)

    return [img,out_final]



def Log_transform(input_image):
    img = Image.open(input_image).convert('L')
    img = img.resize((400,400))

    #img = input_image.resize((400,400), Image.ANTIALIAS)
    numpy_image = np.array(img)
    numpy_image = np.array(img)
    numpy_image = numpy_image/255
    numpy_image = numpy_image + 1
    numpy_image = np.log(numpy_image)
    print(type(numpy_image))
    numpy_image = numpy_image * 255
    numpy_image = np.around(numpy_image,decimals=0)
    log_image = Image.fromarray(numpy_image)
    log_image = log_image.convert("L")

    out_io = BytesIO()
    log_image.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=input_image.name)

    in_io = BytesIO()
    img.save(in_io,'PNG',quality=85)
    img = File(in_io,name=input_image.name)



    return [img,out_final]


def Power_transform(input_image,gamma=2):
    img = Image.open(input_image).convert('L')
    img = img.resize((400,400))

    numpy_image = np.array(img)
    numpy_image = numpy_image/255
    numpy_image_a = np.power(numpy_image,gamma)
    numpy_image_a = numpy_image_a * 255
    numpy_image_a = np.around(numpy_image_a,decimals=0)
    power_image = Image.fromarray(numpy_image_a)
    power_image = power_image.convert("L")


    out_io = BytesIO()
    power_image.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=input_image.name)

    in_io = BytesIO()
    img.save(in_io,'PNG',quality=85)
    img = File(in_io,name=input_image.name)
   

    return [img,out_final]

def Threshold(input_image,threshold=150):
    
    img = Image.open(input_image).convert('L')
    img = img.resize((400,400))

    numpy_image = np.array(img)
    
    row = numpy_image.shape[0]
    column = numpy_image.shape[1]
    new_array = np.zeros(shape=(row,column))

    for i in range(row):
        for j in range(column):
            if(numpy_image[i][j]>=threshold):
                new_array[i][j] = 255 
            else:
                new_array[i][j] = 0
            
    #converting array back to image
    threshold_image = Image.fromarray(new_array)  
    threshold_image = threshold_image.convert("L")


    out_io = BytesIO()
    threshold_image.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=input_image.name)

    in_io = BytesIO()
    img.save(in_io,'PNG',quality=85)
    img = File(in_io,name=input_image.name)
    

    return [img,out_final]


def Negative(input_image):
    img = Image.open(input_image).convert('L')
    img = img.resize((400,400))

    numpy_image = np.array(img)

    row = numpy_image.shape[0]
    column = numpy_image.shape[1]
    new_array = np.zeros(shape=(row,column))
    for i in range(row):
        for j in range(column):
            new_array[i][j] = 255 - numpy_image[i][j]
    
    negative_image = Image.fromarray(new_array)
    
    negative_image = negative_image.convert("L")
    
    
    out_io = BytesIO()
    negative_image.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=input_image.name)

    in_io = BytesIO()
    img.save(in_io,'PNG',quality=85)
    img = File(in_io,name=input_image.name)
    

    return [img,out_final]

def Histogram_equalization(input_image):
    img_main = Image.open(input_image).convert('L')
    img_main = img_main.resize((400,400))


    # # convert our image into a numpy array
    img = np.asarray(img_main)
    # put pixels in a 1D array by flattening out img array
    flat = img.flatten()

    # show the histogram
    #plt.hist(flat, bins=256)

    histogram = np.zeros(256)
    # loop through pixels and sum up counts of pixels
    for pixel in flat:
        histogram[pixel] += 1

    #plt.plot(histogram)

    a = iter(histogram)
    b = [next(a)]
    for i in a:
        b.append(b[-1] + i)

    cs = np.array(b)

    # numerator & denomenator
    nj = (cs - cs.min()) * 255
    N = cs.max() - cs.min()

    # re-normalize the cumsum
    cs = nj / N

    # cast it back to uint8 since we can't use floating point values in images
    cs = cs.astype('uint8')


    # get the value from cumulative sum for every index in flat, and set that as img_new
    img_new = cs[flat]
  

    # put array back into original shape since we flattened it
    img_new = np.reshape(img_new, img.shape)


    histo_image = Image.fromarray(img_new)
    
    histo_image = histo_image.convert("L")


    out_io = BytesIO()
    histo_image.save(out_io,'PNG',quality=85)
    out_final = File(out_io,name=input_image.name)

    in_io = BytesIO()
    img_main.save(in_io,'PNG',quality=85)
    img = File(in_io,name=input_image.name)
    

    return [img,out_final]