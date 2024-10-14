from PIL import Image
from pylab import *
import matplotlib.pyplot as plt

# read image to array
im = array(Image.open('C:\Users\LEVEL51 PC\OneDrive\Pictures\tattoo_design.jpg').convert('L'))

# create a new figure
figure()

# show contours with origin upper left corner
contour(im, levels=[160], colors='black', origin='image')
axis('equal')

plt.savefig("Tattoo_stencils\Take-3-stencil.jpg")
