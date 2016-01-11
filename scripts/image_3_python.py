#! /usr/bin/env python

# Header
'''
:Despription:         Displays a FITS image on a PDF file with annotations

:Execute:
                      >>> python image_3_python.py

:Inputs:              u9w10107m_drz.fits

:Outputs:             images_plot_3.pdf

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
from matplotlib.ticker import MultipleLocator
import numpy as np

# Name output file
psname = '../plots/image_plot_3.pdf'

# Set up plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlabel('x pixels')
ax.set_ylabel('y pixels')
ax.set_xlim(0, 700)
ax.set_ylim(0, 700)

# Read input image and select subarray
image = pf.getdata('../data/u9w10107m_drz.fits', 1)
image = image[100:800, 100:800]

# Define coordinates of sources
xc = [112.40, 194.21, 172.80, 385.57, 152.96, 302.10, 317.19, 195.28, 389.43]
yc = [ 399.14, 443.14,  496.3, 407.87, 677.33, 670.35, 675.82, 473.09, 376.93]

# Plot image and overplot sources
cmap = cm.get_cmap('jet')
img = ax.imshow(image, cmap=cmap, vmin=1, vmax=6, interpolation='bilinear')
ax.plot(xc, yc, marker='o', mec='white', mfc='none', ms=15, ls='none')

# Annotate sources 1 and 2
ax.annotate('1', xy=(xc[0], yc[0]), xytext=(xc[0]+15, yc[0]-5), color='w')
ax.annotate('2', xy=(xc[1], yc[1]), xytext=(xc[1]+15, yc[1]-5), color='w')

# Add a scale
ax.plot([680, 680], [150,300], color='w', lw=2)
ax.text(660, 225, '1 Kpc', color='w', rotation=90)

# Add a colorbar
ax_cb = fig.add_axes([0.2, 0.2, 0.3, 0.025])
cbar = plt.colorbar(mappable=img, cax=ax_cb, orientation='horizontal')

cbar.locator = MultipleLocator(1)
cbar.update_ticks()
cbar.ax.set_xticklabels(np.arange(0, 200, 39))

cbar.outline.set_edgecolor('w')
cbar.ax.xaxis.set_tick_params(color='w')
cbxtick_obj = plt.getp(cbar.ax.axes, 'xticklabels')
plt.setp(cbxtick_obj, color='w')

cbar.ax.invert_xaxis()

# Save figure
fig.savefig(psname)
