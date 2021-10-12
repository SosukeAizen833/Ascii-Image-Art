# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:40:19 2021

@author: Space
"""
#%%
from PIL import Image
import numpy as np
import math
im = Image.open('ascii-pineapple.jpg')

im.thumbnail((200,150));



print(im.format,im.size,im.mode)
h = im.size[0]
w=im.size[1]
print(h,w)

#%%
image_sequence = im.getdata()
image_array = np.array(image_sequence)

def avg(arr):
    sum = 0;
    for x in range(len(arr)):
        sum += arr[x]
    n = len(arr)
    return sum/n;


brightness_array = np.zeros(len(image_array))
print(len(brightness_array))
for x in range(len(image_array)):
    brightness_array[x] = avg(image_array[x])

ascii_string = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
print(len(ascii_string))

#%%
normalized_arr = []

for x in range(len(brightness_array)):
    normalized_arr.append(math.floor(brightness_array[x]/(255/len(ascii_string))))

print(len(normalized_arr))

asci_arr = []
for x in range(len(normalized_arr)):
    i = int(normalized_arr[x])
    asci_arr.append(ascii_string[i])
    
for i in range(w):
    for j in range(h):
        print(asci_arr[i*h+j]*6,end='')
    print('\n')
print(len(normalized_arr))

