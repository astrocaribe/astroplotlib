"""
:Description:   Displays a bar plot

:Execute:
                >>> python histogram_4_python

:Inputs:        input data

:Outputs:       histogram_4.pdf

:Autor:         Tommy Le Blanc
                https://github.com/astrocaribe

:Revisions:
                - Written by Tommy LEBLANC, Dec 2012
                - Tweaked plot display, Jul 2013
                - Misc updates, Dec 2015
"""

# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np

# Name output file
psName = '../plots/histogram_4.pdf'

# Create data and labels for the bar plot.
data1 = [1, 0.6, 0.8]
data2 = [0.85, 0.4, 0.95]
labels = ['0.4 Z$_\odot$', '1 Z$_\odot$', '2.5 Z$_\odot$']

# Set up plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-0.1, 2.7, plt.minorticks_off())
ax.set_ylim(0., 1.2, plt.minorticks_on())

ind = np.arange(len(data1))
width = .3

# Plot bars
ax.bar(ind, data1, width, color='darkslateblue', ec='white')
ax.bar(ind+width, data2, width, color='royalblue', ec='white')

# Add axes labels and titles (x), and annotations
ax.set_xlabel('Metallicity', size=18)
ax.set_ylabel('Normalized Frequency', size=18)


ax.set_xticks(ind+width)
ax.set_xticklabels(labels, size=18)
for t in ax.get_yticklabels(): t.set_fontsize(18)

ax.annotate(' inner disk', xy=(1.15, 0.65),  xycoords='data',
            xytext=(1.15, 1.1), textcoords='data',
            arrowprops=dict(facecolor='black', width=0.1, headwidth=5),
            horizontalalignment='center', verticalalignment='top',
            rotation=90, size='xx-large'
            )

ax.annotate(' outer galaxy', xy=(1.45, 0.45),  xycoords='data',
            xytext=(1.45, 1.1), textcoords='data',
            arrowprops=dict(facecolor='black', width=0.1, headwidth=5),
            horizontalalignment='center', verticalalignment='top',
            rotation=90, size='xx-large'
            )

# Save figure
fig.savefig(psName)
