import sys
import numpy
from astropy.time import Time
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.coordinates import AltAz
from astropy.coordinates import EarthLocation

### converts (Ra, Dec, JD) to (Az, Alt, UTC) for Mt. Stony Brook

# the first argument is the name of the input file (text file, 3 columns: Ra, Dec, JD)
# the second argument is the name of the output file (text file, 3 columns: azimuth, altitude, UTC)

input=sys.argv[1]
output=sys.argv[2]

# location of Stony Brook
observing_location = EarthLocation(lat=40.914224*u.deg, lon=-73.11623*u.deg, height=0)

# read in the input file
transits=numpy.loadtxt(input)

# define the Ra, Dec pairs
coords=SkyCoord(transits[:,0]*u.deg,transits[:,1]*u.deg, frame='icrs')

# define the observing times
times=Time(transits[:,2], format='jd')

# do the transformation to AltAz
aa = AltAz(location=observing_location, obstime=times)
aacoords=coords.transform_to(aa)

# specify output timeformat to be in UTC
times.format='fits'

# write output file
numpy.savetxt(output,numpy.transpose([aacoords.az,aacoords.alt,times]), fmt="%.6f %.6f %.30s")
