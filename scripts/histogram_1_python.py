#! /usr/bin/env python

# Header
"""
:Description:   Plots a simple outline histogram from a given set of numbers

:Execute:
                >>> python histogram_1_python

:Inputs:        master.xy

:Outputs:       histogram_1.pdf

:Autor:         Tommy Le Blanc
                https://github.com/astrocaribe

:Revisions:
                - Written by Tommy LEBLANC, Dec 2012
                - Tweaked plot display, Jul 2013
                - Misc updates, Dec 2015
"""

# Import necessary modules
import numpy as np
import matplotlib.pyplot as plt
# Name output file
psName = '../plots/histogram_1.pdf'

# Read input data and calculate number of bins
xref, yref, mag = np.loadtxt('../data/master.xy', usecols = (0, 1, 2), unpack = True)

min_mag, max_mag = np.min(mag), np.max(mag)
binsize = 0.2
num_bins = np.floor((max_mag - min_mag) / binsize)

# Create histogram, figure size in inches
fig, ax = plt.subplots(figsize = (6, 6))

# Define axes
ax.set_xlabel('Mag', size=12)
ax.set_ylabel('Histogram Density', size=12)
ax.set_xlim(-17., -6.)
ax.set_ylim(0., 2800.)

for t in ax.get_xticklabels(): t.set_fontsize(12)
for t in ax.get_yticklabels(): t.set_fontsize(12)

# Draw histogram
ax.hist(mag, num_bins, color='red', lw=2,  histtype='step')

# Save plot as a PDF file
fig.savefig(psName)
