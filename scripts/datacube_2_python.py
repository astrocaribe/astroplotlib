#! /usr/bin/env python
# coding=utf-8

# Header
"""
:Description:   Displays the spectrum of one pixel of a datacube

:Execute:
                >>> python datacube_2_python

:Inputs:        ngc4151_hband.fits

:Outputs:       datacube_2.pdf

:Autor:         Tommy Le Blanc
                https://github.com/astrocaribe

:Revisions:
                - Written by Tommy LEBLANC, Dec 2012
                - Tweaked plot display, Jul 2013
                - Misc updates, Dec 2015
"""

# Import necessary modules
import pyfits as pf
import matplotlib.pyplot as plt
import numpy as np

# Name output file
psname = '../plots/datacube_2.pdf'

# Read datacube
# This datacube is not continuum subtracted
cube, hdr = pf.getdata('../data/ngc4151_hband.fits', header=True)

# Calibrate wavelength from header keywords
crpix3 = hdr['CRPIX3']
cdelt3 = hdr['CDELT3']
crval3 = hdr['CRVAL3']

tam = cube.shape

pixel = np.arange(tam[0]) + 1.0
lamb = crval3 + (pixel - crpix3) * cdelt3

# Select pixel with coodinates [30, 30] in range of datacube
flux = cube[100:1900, 30, 30]
lambda_microns = lamb[100:1900] / 1.e4

# Setup plot
fig, ax = plt.subplots(figsize = (12, 4))

ax.set_xlabel('wavelength ('+'$\mu$'+'m)', size=12)
ax.set_ylabel('flux', size=12)
ax.minorticks_on()
ax.set_xlim([min(lambda_microns), max(lambda_microns)])
ax.set_ylim([min(flux), max(flux)])

# Plot spectrum
ax.plot(lambda_microns, flux, color='red', lw=1)

# Save figure
fig.savefig(psname, orientation='landscape')
