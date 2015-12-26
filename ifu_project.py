#! /usr/bin/env python

# Header

__author__ = 'T.S. Le Blanc'
__version__ = 0.1

'''
ABOUT:
	This script was written to complete the final training data
	project for STScI. The following goals for completion are
	as follows:
	1) Recreate the continuum subtracted Fe [II] line emission 
	   panels from Fig 6. in the Storchi-Bergmann et al. 
	   2006 Paper I, using the IDL training module on IFUs as a
	   template.
	2) Display the central pixel of the IFU as a function of
	   wavelength and make an appropriate measurement of the
	   intensity of the Fe[II] line in Fig. 6 (see previous goal).
	3) Attempt to make code generic enough to measure the
	   of any line fed into the script (see the above 2 points).   
'''

# Load needed packages
import argparse as ap
import pdb
import numpy as np
import pyfits as pf
import pylab as pl
#import NIRSpec_Tools as nst


# ********************** Definitions **********************

def frame_conv(frame):
    ''' 
	Convert the frame to a wavelength using a starting value and 
    delta (in microns) specific to the NGC4151_Hband.fits file
    '''
    
    # Constants
    crval = 1.47664
    cdelt = 0.00016
    
    # Calculate the frame conversion
    wave = frame * cdelt + crval
    
    return wave
    
    
def wave_conv(wave):
    '''
    Convert the wavelength to a frame using a starting value and 
    delta (in microns) specific to the NGC4151_Hband.fits file 
    '''
    
    from numpy import round
    from numpy import int

    # constants
    crval = 1.47664
    cdelt = 0.00016

    # Calculate the wavelength conversion
    frame = (wave - crval) / cdelt
    
    return int(round(frame))
    
 
# **************************** Main ****************************

if __name__ == '__main__':

    #provide command-line help
    parser = ap.ArgumentParser(description='Measure intensity of \
      a spectral line.')
    parser.add_argument('-f', '--file', default='', type=str, \
      help='Input file.')
    options = parser.parse_args()
    
    #open input file and extract data
    infile = options.file
    print 'Opening ', infile, ' ...'
    print
    f = pf.open(infile)
    fcube = f[1].data
    fheader = f[1].header
    f.close()

    print 'Data cube dimensions (x, y, lambda):'
    print fheader['NAXIS1'], fheader['NAXIS2'], fheader['NAXIS3']
    print

    #create an array to store the pixel calibrations
    pixel = np.array([x+1 for x in range(fheader['NAXIS3'])])
    
    #calibrate the 3 dimensions of the image...
    #for x...
    crpix1 = fheader['CRPIX1']
    cdelt1 = fheader['CDELT1']
    crval1 = fheader['CRVAL1']
    cunit1 = fheader['CUNIT1']
    x = crval1 + (pixel - crpix1) * cdelt1
    
    #for y...
    crpix2 = fheader['CRPIX2']
    cdelt2 = fheader['CDELT2']
    crval2 = fheader['CRVAL2']
    cunit2 = fheader['CUNIT2']
    y = crval2 + (pixel - crpix2) * cdelt2

    #and for lambda...
    crpix3 = fheader['CRPIX3']
    cdelt3 = fheader['CDELT3']
    crval3 = fheader['CRVAL3']
    cunit3 = fheader['CUNIT3']
    lamb = crval3 + (pixel - crpix3) * cdelt3

    #generate the spectrum of a given pixel
    #select the central pixel (x=y=30)
    image = fcube[100:1900, 30, 30]
    
    #convert wavelength from angs to microns
    wavelength = lamb[100:1900] / 1.e4
    print len(wavelength)
    
    #compute an estimate for the continuum
    p = np.polyfit(wavelength, image, 1)
    print 'Gradient and y-intercept:'
    print p
    y = p[0] * wavelength + p[1]
    
    #compute continuum-subtracted spectrum
    z = image - y
    
    #plot the original spectrum, as well as the continuum-
    #subtracted, and save to an external file
    outfile = 'Spectrum.pdf'
    pl.plot(wavelength, image, 'r-', linewidth = .5)
    pl.plot(wavelength, y, 'k--', linewidth = 1)
    pl.plot(wavelength, z, 'b-', linewidth = .5)
    pl.legend(('Spectrum','Continuum','Continuum-subtracted'), \
      'best')
    pl.xlabel('Wavelength (microns)')
    pl.ylabel('Flux')
    pl.savefig(outfile)
    pl.clf()
    print 'File saved to: ', outfile
    
    # Create a new continuum-subtracted slice, generating a
    # compressed image ~ 1.644 micron, including double-peaked
    # feature (frame[0] - frame[1])
    frame = np.array([1067, 1083])
    #cmp_image = np.zeros(len(fcube[:,0:,0]))
    
    print len(fcube[:,0:,0]), len(fcube[:,0:,0]), len(fcube[:,0:,0])
    pdb.set_trace()
    
    print frame_conv(frame[0])
    print frame_conv(frame[1])
    
    
    