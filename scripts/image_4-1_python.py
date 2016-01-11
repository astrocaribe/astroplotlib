#! /usr/bin/env python

# Header
'''
:Despription:         Shows the use of colour tables

:Execute:
                      >>> python image_4-1_python.py

:Inputs:              proplyd.fits

:Outputs:             images_plot_4-1.pdf

:Author:              Tommy LE BLANC
                      Space Telescope Science Institute, USA

:Revisions:
                      - Written by Tommy LE BLANC, Jul 2013
                      - Misc updates, Jan 2016
'''

# Import necessary modules
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pyfits as pf
import numpy as np

# Name output file
psname = '../plots/image_plot_4-1.pdf'

# Read FITS file
img = pf.getdata('../data/proplyd.fits', 0)

# Setup plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
ax1.set_aspect('equal')
ax2.set_aspect('equal')
ax1.set_xlabel(r'$\Delta \alpha$ ["]')
ax1.set_ylabel(r'$\Delta \delta$ ["]')
ax1.set_title('Disk 114-426')
ax2.set_title('345 GHz')
ax2.set_xlabel(r'$\Delta \alpha$ ["]')

# Plot left figure
cmap = cm.get_cmap('gist_heat_r')
ax1.imshow(img, cmap=cmap, vmin=0, vmax=6, extent=[4,-4,-4,4], origin='lower')

# Plot right figure
# Compute contours
contour_x = 4.0 - np.arange(90)* ((4.0 - (-4.0))/89.)
contour_y = -4.0 + np.arange(90)* ((4.0 - (-4.0))/89.)
ax2.set_xlim(4,-4)

# Set cmap colour scheme
cmap = cm.get_cmap('jet')

levels = [0.0, 0.6, 0.8, 0.9,1.0, 1.2, 2.0, 3.0, 5.0, 7.0]
cont = ax2.contourf(contour_x, contour_y, img, cmap=cmap, vmin=0.1, vmax=3, levels=levels)
ax2.ticklabel_format(axis='y', visible='False')

# Save figure
fig.savefig(psname)
