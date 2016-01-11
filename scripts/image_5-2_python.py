#! /usr/bin/env python

# Header
'''
:Despription:         Displays an ACS footprint on a DSS image. No geometric distortion applied

:Execute:
                      >>> python image_5-2_python.py

:Inputs:              m101_blue.fits

:Outputs:             images_plot_5-2.pdf

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

from astropy.wcs import WCS
from astropy.io import fits

from matplotlib.path import Path
import matplotlib.patches as patches

# Name output file
psname = '../plots/image_plot_5-2.pdf'

# Set up plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlabel('x pixels')
ax.set_ylabel('y pixels')

# Read in image and calcualte size
image, header = pf.getdata('../data/m101_blue.fits', 0, header=True)
tam = image.shape
ax.set_xlim(0, tam[0])
ax.set_ylim(0, tam[1])

# Generate plot
cmap = cm.get_cmap('gist_gray')
ax.imshow(image, cmap=cmap, interpolation='nearest')
# ax.invert_yaxis()

# Read both ACS chip pix coordinates (extensions 1 and 4)
hdulist = fits.open('../data/j8d602gxq_flt.fits')
hdu1 = hdulist[1]
hdu4 = hdulist[4]
hdulist.close()

# Read image coordinates
hdulist_image = fits.open('../data/m101_blue.fits')
hdu_image = hdulist_image[0]
wcs_image = WCS(hdu_image.header)
hdulist_image.close()

# Chip dimensions
chipXdims = [0.0, 4096.0, 4096.0, 0.0]
chipYdims = [0.0, 0.0, 2048.0, 2048.0]

# Use WCS to calculate celestial coordinates for chips 1 and 4
wcs1 = WCS(hdu1.header)
wcs4 = WCS(hdu4.header)
ra_1, dec_1 = wcs1.wcs_pix2world(chipXdims, chipYdims, 1)
ra_2, dec_2 = wcs4.wcs_pix2world(chipXdims, chipYdims, 1)

# Use WCS to calculate pix coordinates for image
chip_1_x, chip_1_y = wcs_image.wcs_world2pix(ra_1, dec_1, 1)
chip_2_x, chip_2_y = wcs_image.wcs_world2pix(ra_2, dec_2, 1)

# Create footprint shapes via matplotlib.path
chip1Path= zip(*[chip_1_x, chip_1_y]); chip1Path.append(chip1Path[0])
chip2Path= zip(*[chip_2_x, chip_2_y]); chip2Path.append(chip2Path[0])
chipFootprint = chip1Path + chip2Path

# Plot chip footprints using Path, patches
codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY] * 2
path = Path(chipFootprint, codes)
patch = patches.PathPatch(path, edgecolor='orange', lw=1, fill=False)
ax.add_patch(patch)

# Save figure
fig.savefig(psname)
