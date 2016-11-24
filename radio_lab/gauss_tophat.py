#! /usr/bin/python

import math
import matplotlib.pyplot as plt
import numpy

# Defines gaussian function with standard deviation (full-width as half maximum) sigma
def gaussian(x,sigma):
    return 1/(2*math.sqrt(2*math.pi)) * math.exp(-(x/(2*sigma))**2)

n=1000 # number of points
t=0.001 # sampling interval
fwhm = 0.033 # radians (1.22 * 2.7 cm / 1.0 m)
resolved_source_width = 1.0 # radians (make it an even # of t's)
                            # exaggerated: actual solar value is
                            # 0.01 rad
# define n dimensional vector of the gaussian function evaluated over the sampling interval 
gaus = [gaussian( (i- n/2.0 + 1)*t, fwhm ) for i in range(n)]

# define top hat over sampling interval
tophat = [0]*n

for i in range(n):
    if(i**2<(resolved_source_width/t/2)**2):
        tophat[i] = 1.0

# Convolution of guassian and top hat
gauss_hat = numpy.convolve(gaus, tophat)

# plot results
y = [(i- n/2.0 + 1)*t/2 for i in range(2*n-1)]

plt.xlim(-0.2,0.5)
plt.plot(y,gauss_hat)

plt.show()

print gauss_hat

#print x



 
