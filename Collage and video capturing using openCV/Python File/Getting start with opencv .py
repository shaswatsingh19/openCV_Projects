#!/usr/bin/env python
# coding: utf-8

# 
# #  In this notebook we are learning open cv 
# 

# In[1]:


# openCV is used to store , manuplate images 
# with this we can crop image , change color of images 
# used toremove noise from images or contrast and much more
# can be done with opencv 


# In[2]:


# Let's start by importing cv2 , which contain all the functionality of opencv
import cv2


# In[23]:


img = cv2.imread("image/test1.jpg")
print(img)
# after printing you can see the pixel of the images or matrix 
# it is a matrix data structure and as you can see
# it is divided into three column eg [ 155 117 35 ]
# these are the values of RGB at every pixel 
# and in python it is a numpy array


# In[24]:


# Now we want to show image so we use matplotlib function which has the imshow()
# imshow function
import matplotlib.pyplot as plt

plt.imshow(img)
plt.show()
# But there is a little problem here if you see the test1 in image folder it is different than the current output
# it is because in opencv we use BGR format to store image but in matplotlib it is RBG 
# it means  all the pixel are exchange in cyclic form 
# to change that we use one of the cv2 function which is cvtColor which change BGR to RBG colorspace

img1 = cv2.imread("image/test1.jpg")
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.show()
# now the exact image shows here


# In[6]:


# we are checking the (height , width , depth ) of that test1.jpg images
# here height and width are y and x axis of image and depth = 3 
print(img.shape)


# In[50]:


# this given image is a special type of data type which is a numpy array 
# now let's see little about numpy array
# here array is the function in the numpy module 
# in this we pass that array or
import numpy as np
ar = np.array([[[1,2,3],
                [4,5,6],
                [7,8,9]]])
print(ar)
print("Numpy array shape is :",ar.shape)


# In[8]:


print(ar[0][2][1])
# Which is 2nd row and we know that count start from 0
# [2][1] is 3rd row and 2nd column which is 8


# In[47]:


# now if we want to read all the images in the file 
# let's say 1000 image we can't write every for it 
# so we use loop 
# but first we are using os library to read file
# os means operating system which use to read and write to files 
import os

images = os.listdir("image")
print(images)
print()
for f in images:
    
    print("THE IMAGE TO PRINT IS" ,f)
    
    file_path = "image/" +f
    
    img = cv2.imread(file_path)
    
    # BGR colorspace
    print("BGR COLOR SPACE")
    plt.imshow(img)
    
    # we are using title() to show on the top of image
    # here we are showing it shape
    plt.title(img.shape)
    plt.show()
    
    # RGB colorsplace
    print("CONVERTS TO RGB COLOR SPACE")
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title(img.shape)
    plt.show()
    
    


# In[149]:


# Now let's create a collage of the images

red = np.zeros((50,50,3),dtype ='int')
red[:,:,0] = 255


green = np.zeros((50,50,3),dtype ='int')
green[:,:,1] = 255


blue = np.zeros((50,50,3),dtype ='int')
blue[:,:,2] = 255

plt.imshow(red)
plt.show()


plt.imshow(green)
plt.show()


plt.imshow(blue)
plt.show()


# # 

# In[146]:


# we have t combine to make a collage
red_green = np.hstack((red,green))
plt.imshow(red_green)
plt.show()
green_red = np.hstack((green,red))
plt.imshow(green_red)
plt.show()

combine = np.vstack((red_green,green_red))
plt.imshow(combine)
plt.show()


# In[145]:


# now let's make our image collage using previous
import os

images = os.listdir("image")
print(images)
print()
heros = []
for f in images:
    
    print("THE IMAGE TO PRINT IS" ,f)
    
    file_path = "image/" +f
    
    img = cv2.imread(file_path)
 
    # RGB colorsplace
    print("CONVERTS TO RGB COLOR SPACE")
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# let's resize all image in one size
    img = cv2.resize(img,(900,900))
    heros.append(img)


# now make a collage

hero_12 = np.hstack((heros[0],heros[1]))
hero_34 = np.hstack((heros[2],heros[3]))
collage  = np.vstack((hero_12,hero_34))

plt.imshow(collage)
plt.show()


# In[ ]:




