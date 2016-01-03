#! /usr/bin/env python

# Header
"""
:Description:   Plots random data as red squares. Obtains a linear fit and overplots the fit.

:Execute:
                >>> python simple_plot_3_python

:Inputs:        numpy random numbers

:Outputs:       simple_plot_3.pdf

:Autor:         Tommy Le Blanc
                https://github.com/astrocaribe

:Revisions:
                - Written by Tommy LEBLANC, Dec 2012
                - Tweaked plot display, Jul 2013
                - Misc updates, Dec 2015
"""

# Name output file
psName = '../plots/simple_plot_3.pdf'

# Import necessary modules
import pyfits as py
import matplotlib.pyplot as plt
import numpy as np

# Define some random data
np.random.seed(5)
x = np.random.standard_normal(400) * 12.
np.random.seed(1)
y = x + np.random.standard_normal(len(x))

# Perform a line fit to the data
line = np.polyfit(x, y, 1)

# Define x-values for line fit
x_fit = np.arange(21)
y_fit = line[0] * x_fit + line[1]

# Setup plot, size in inches
fig, ax = plt.subplots(figsize = (4.724, 4.724))

# Define axes
ax.set_xlabel('x title')
ax.set_ylabel('y title')
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)

# Plot data
ax.plot(x, y, marker='s', mec='r', mfc='r', ls='none', alpha=0.7)
ax.plot(x_fit, y_fit, 'b--')

# Save figure
fig.savefig(psName)
