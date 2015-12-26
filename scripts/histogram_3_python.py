#! /usr/bin/env python

# Header
"""
:Description:   Creates a simple rotated histogram from a given set of numbers

:Execute:
                >>> python histogram_3_python

:Inputs:        numpy random numbers

:Outputs:       histogram_3.pdf

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
psName = '../plots/histogram_3.pdf'

# Generate random input data, and calculate number of bins based on binsize
np.random.seed(1)
data = np.random.randn(500) * 25

min_data, max_data = np.min(data), np.max(data)
binsize = 5.
num_bins = np.floor((max_data - min_data) / binsize)

# Create histogram
fig, ax = plt.subplots(figsize = (6, 6))

# Define axes
ax.set_xlabel('N', size=12)
ax.set_ylabel('data', size=12)
for t in ax.get_xticklabels(): t.set_fontsize(12)
for t in ax.get_yticklabels(): t.set_fontsize(12)

# Draw histogram
n, bins, patches = ax.hist(data, num_bins, fc='darkred', ec='darkred', orientation='horizontal')
for b in patches[::2]: b.set_facecolor('red')

# Save plot as a PDF file
fig.savefig(psName)
