#! /usr/bin/env python

# Header
'''
:Despription:         Displays a contour on a FITS image background

:Execute:
                      >>> python contours_3_python.py

:Inputs:              m101_blue.fits

:Outputs:             contours_3.pdf

:Author:              Tommy LE BLANC
                      Space Telescope Science Institute, USA

:Revisions:
                      Written by Tommy LE BLANC, JUL 2013.
'''

# Import necessary modules
import numpy as np
import pyfits as pf
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Name the output file
psName = '../plots/contours_3.pdf'

# Setup plot and axes
fig, ax = plt.subplots(figsize=(6, 6))

# Turn off axes labels
ax.set_xticklabels([])
ax.set_yticklabels([])

# Read in image data
image = pf.getdata('../data/m101_blue.fits')

# Select a subarray
image = image[300:800, 300:800]

# Scale input image
bottom, top = 0., 18000.
data = (((top - bottom) * (image - image.min())) / (image.max() - image.min())) + bottom

# Determine image dimensions
tam = np.size(data, axis=0)

# Select image colour map
cmap = cm.get_cmap('gist_heat_r')

# Display image
im = ax.imshow(data, cmap=cmap)
ax.invert_yaxis()

# Calculate contours
contour_x = np.arange(tam)
contour_y = np.arange(tam)

# Set contour levels
colors = ['forestgreen','green', 'limegreen']
levels = [7500., 12000., 15000.]

# Display contours
cnt = plt.contour(contour_x, contour_y, data, colors=colors, levels=levels, linewidths=1.0)

# Save image
fig.savefig(psName)
