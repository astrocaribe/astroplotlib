#! /usr/bin/env python

# Header
"""
:Description:   Displays several spectra read from a FITS file.
                Displays a plot within a plot.

:Execute:
                >>> python spectra_2_python

:Inputs:        ckp00_25000.fits
                ckp00_30000.fits
                ckp00_32000.fits
                ckp00_33000.fits
                ckp00_34000.fits
                ckp00_35000.fits
                ckp00_36000.fits
                ckp00_37000.fits
                ckp00_38000.fits
                ckp00_39000.fits
                ckp00_40000.fits

:Outputs:       spectra_2.pdf

:Autor:         Tommy Le Blanc
                https://github.com/astrocaribe

:Revisions:
                - Written by Tommy LEBLANC, Dec 2012
                - Tweaked plot display, Jul 2013
                - Misc updates, Dec 2015
"""

# Import ncessary modules
import numpy as np
import pyfits as pf
import matplotlib.pyplot as plt

# Name the output file
psname = '../plots/spectra_2.pdf'

# Set up plot (symbols in LaTeX Math Mode)
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlabel('$\lambda (\AA)$', size='x-large')
ax.set_ylabel('$F_\lambda (10^{-11} \ ergs \ cm^{-2} \ s^{-1} \ \AA^{-1})$', size='x-large')
ax.set_xlim(200., 3000.)
ax.set_ylim(0., 2.2)
for t in ax.get_xaxis().get_major_ticks(): t.set_pad(12.)

# Plot 10 kurucz models
teff = ['40000', '39000', '38000', '37000', '36000', '34000', '33000', '32000', '30000', '25000']
for k in xrange(len(teff)):
    spect1 = pf.getdata('../data/ckp00_' + teff[k] + '.fits', 1)
    x = spect1.field('wavelength')
    y = spect1.field('g45')
    ax.plot(x, y / 1.e11, color='#084B93')

# Emphasize the 35000K model (11th) in red
spect1 = pf.getdata('../data/ckp00_35000.fits', 1)
x = spect1.field('wavelength')
y = spect1.field('g45')
ax.plot(x, y / 1.e11, color='salmon')

# Add a flux axis in log scale on the right
ax_log = ax.twinx()
y1, y2 = ax.get_ylim()
ax_log.set_ylim(10.**y1, 10.**y2)
ax_log.figure.canvas.draw()
ax_log.set_yscale('symlog')

# Define random data to plot
data = np.random.randn(1000)

# Plot inset of fake random data
ax_inset = plt.axes([.67, .45, .2, .4])
ax_inset.set_xlim(-4,4)
ax_inset.set_ylim(0, 55)
ax_inset.set_ylabel('N', size='large')
ax_inset.hist(data, bins=70, color='salmon', histtype='step')

# Save figure
fig.savefig(psname, orientation='landscape')
