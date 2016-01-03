#! /usr/bin/env python
# coding=utf-8

# Header
"""
:Description:   Displays a contour plot on a datacube slice

:Execute:
                >>> python datacube_1_python

:Inputs:        ngc4151_hband.fits

:Outputs:       datacube_1.pdf

:Autor:         Tommy Le Blanc
                https://github.com/astrocaribe

:Revisions:
                - Written by Derek HAMMER and Tommy LEBLANC, Dec 2012
                - Tweaked plot display, Jul 2013
                - Misc updates, Dec 2015
"""

# Import necessary modules
import pyfits as pf
import matplotlib.pyplot as plt
import numpy as np

# Name the output file
psname = '../plots/datacube_1.pdf'

# Read datacube
cube, header = pf.getdata('../data/ngc4151_hband.fits', header=True)

# We plot slice 1067
cube_slice = 1067
image = cube[cube_slice, :, :]
tam = image.shape

# Display the background image
cmap = plt.cm.get_cmap('hot')
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(image, cmap=cmap, vmin = 0, vmax = 100, interpolation='nearest')

# Define axes
ax.set_xlabel('x pixels')
ax.set_ylabel('y pixels')
ax.set_ylim([0, tam[0]-1])
ax.set_xlim([0, tam[1]-1])

# Create contours
contour_x = np.arange(tam[0])
contour_y = np.arange(tam[1])
levels = [5., 10., 20., 30., 40., 50., 100., 200., 600.]
contour_lines = ax.contour(contour_x, contour_y, image, colors='lime', levels=levels)
plt.clabel(contour_lines, inline=1, fontsize=6, fmt='%2d')

# Save figure
fig.savefig(psname)
