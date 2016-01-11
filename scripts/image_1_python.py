#! /usr/bin/env python

# Header
'''
:Despription:         Displays a FITS image on a PDF file

:Execute:
                      >>> python image_1_python.py

:Inputs:              ib6w71lxq_flt.fits

:Outputs:             images_plot_1.pdf

:Author:              Tommy LE BLANC
                      Space Telescope Science Institute, USA

:Revisions:
                      - Written by Tommy LE BLANC, Jul 2013
                      - Misc updates, Jan 2016
'''

# Import neccesary modules
import pyfits as pf
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Name output file
psname = '../plots/image_plot_1.pdf'

# Set up plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlabel('x pixels')
ax.set_ylabel('y pixels')

# Read in image and select subarray
image = pf.getdata('../data/ib6w71lxq_flt.fits', 4)
image = image[700:1400, 2000:2700]
tam = image.shape

# Generate plot
cmap = cm.get_cmap('gist_gray_r')
ax.imshow(image, cmap=cmap, vmin=0, vmax=100,
          interpolation='nearest')
ax.set_xlim(0, tam[1], plt.minorticks_on())
ax.set_ylim(0, tam[0], plt.minorticks_on())

# Save figure
fig.savefig(psname)
