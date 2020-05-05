#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
import matplotlib.pyplot as plt


# In[15]:


# making camera object
camera = cv2.VideoCapture(0)

# reading the pic
# we are using two variable because we are getting two values
# first one say true if picture captured else false
# pic represent the picture
success , pic = camera.read()

# closing the camera
camera.release()

# showing the image
print(pic)
if success:
    # but the picture will be in BGR format 
    # so convert into RGB
    print("THE IMAGE IS IN BGR : ")
    plt.imshow(pic)
    plt.show()
    
    print("THE NEW IMAGE IS IN RGB : ")
    pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
    plt.imshow(pic)
    plt.show()


# In[ ]:




