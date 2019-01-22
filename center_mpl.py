import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread("sun1.png")
lum_img = img[:,:,0]
print (lum_img.shape)
plt.hist(lum_img.flatten(), 256, range=(0.0,1.0), )
plt.show()

