# astroplotlib
## Revision 1.1

## Purpose
[astroplotlib](http://astroplotlib.stsci.edu/) is a multi-language astronomical library of plots that serves as a template for producing paper-quality plots using IDL, Python, and Mathematica.

I was blessed in participating in this project when I started at the [Space Telescope Science Institute](http://www.stsci.edu) back in 2012, and was the reason (or rather, the excuse) to move from IDL to Python. This is where I began my Python journey, and most recently a return point after a year away coding in other languages (Ruby, Ruby on Rails, Node.js, React.js).

This repo houses the Python script contributions I made for STScI astroplotlib, more info [here](http://astroplotlib.stsci.edu/). I will continue to update this repo with more useful plots, and will be happy to take any suggestions for additional plots types you'd like to see in Python.

## Uses
There are three ways to view the scripts in this repo for your perusal:

1. You can simply checkout the the `scripts` folder and view each individual script. The plots in the `plots` directory can serve as a guide to the naming convention (and output) of the scripts therein.

2. There is a `notebook` folder that contains iPython/Jupyter notebooks (more information on iPython/Jupyter notebooks [here](http://jupyter.org/)). With these individual notebooks, you can run these scripts inline within a browser, usually with no additional setup necessary<sup>1</sup>. Make sure you have iPython notebook installed (I have not yet used/migrated to Jupyter), download the notebook of interest locally, and have at it!

3. Alternatively, the notebooks can be viewed, but not executed, within GitHub directly. This way, there is nothing to install and execute, no data necessary to download, but still gives you the ability to follow along w/ how to produce your favourite plot! I have provided links in the `Structure` section of the README below, or just view directly in the GitHub repo! No fuss, no muss!

#### Disclaimer:
The only missing piece in this repo is the actual data. The reason is an unfortunate, but a very reasonable one: GitHub does not allow file size greater than 100MB. Please refer to the [GitHub Help](https://help.github.com/articles/working-with-large-files/) pages for the very sensible reason for the file size limit restriction.

To obtain the data necessary to execute there scripts, they are currently freely available at the [STScI Astroplotlib]() site; select the plot type, choose the plot, and click on the `download plot` link. The data will be included in the .zip file.

## Plots
The following type of plots are currently represented in this repo, with more to come in the future:

- [Simple Plots](https://github.com/astrocaribe/astroplotlib/blob/master/notebooks/simple%20plot.ipynb) -
  Simple plots including random points along a line, to stellar relationships using different colours, symbols, and even opacity.
- [Histograms](https://github.com/astrocaribe/astroplotlib/blob/master/notebooks/histograms.ipynb) -
  From traditional, simple outline histograms, to multi-colour and orientation varieties. Also includes a bar plot template with labels, and a scatter plot/histogram combo example.
- [Datacubes](https://github.com/astrocaribe/astroplotlib/blob/master/notebooks/datacubes.ipynb) -
  Display datacube information (3D spatial data) by plotting a single frame (x:y frame at z[i], for example), as well as a single point (or an area), such as x[0-10]:y[0-10] for all z.
- [Spectra](https://github.com/astrocaribe/astroplotlib/blob/master/notebooks/spectra.ipynb) -
  Plot spectral information (modeled stellar energy distributions (or SEDs)), along with accompanied image for comparison.
- [Contour Plots](https://github.com/astrocaribe/astroplotlib/blob/master/notebooks/contours.ipynb) -
  Plots of `heat maps`, of sort. Analyse the composition and concentration of gas in an image, for example. View contour values, with simple plot axes, as well as astronomical coordinates for your plots.

## Revision History:
Notes on revisions and/or additions to scripts and notebooks in this repo.

* 1.0, Dec 2012, Jul 2013  
Original creation of scripts

* 1.1, Dec 2015  
Cleanup and light optimization of scripts, as well as compatibility updates.



## Footnotes:
1. Your milage may vary. Please refer to the [Jupyter Notebook](http://jupyter.org/) website for installation instructions.
