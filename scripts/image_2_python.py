#! /usr/bin/env python

# Header
'''
:Despription:         Reads and display a JPEG file

:Execute:
                      >>> python image_2_python.py

:Inputs:              soho_image.jpg

:Outputs:             images_plot_2.pdf

:Author:              Tommy LE BLANC
                      Space Telescope Science Institute, USA

:Revisions:
                      - Written by Tommy LE BLANC, Jul 2013
                      - Misc updates, Jan 2016
'''

# Import necessary modules
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Name output file
psname = '../plots/image_plot_2.pdf'

# Import JPEG and flip top/bottom
image = Image.open('../data/soho_image.jpg')
image = np.array(image.transpose(1))

# Set up plot
fig = plt.figure(figsize=(6, 12))
ax_image = plt.axes([.1, .1, .8, .5], frameon=False)
ax_inset = plt.axes([.1, .57, .4, .2], frameon=False)
ax_image.set_axis_off()
ax_inset.set_axis_off()

# Display main image and inset location
ax_image.plot(850, 850, marker='s', mec='lime', mfc='none',ms=100, mew=1.2)
ax_image.imshow(image)

# Display inset
sub_image = image[700:1000, 700:1000, :]
ax_inset.plot(150, 150, marker='s', mec='lime', mfc='none', ms=172, mew=2)
ax_inset.imshow(sub_image)

# Save output file
fig.savefig(psname)
