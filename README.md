## ak135 Travel Time Ellipticity Correction

This repo was started from ftp://rses.anu.edu.au/pub/ak135/.

We simply exposed a python shared object for `ak135` travel time ellipticity 
correction. 

### How to use

Set the `ELLIPCORR` environment variable:

    export ELLIPCORR=/path/to/ellip-corr 

Then run:
    
    cd /path/to/ellip-crr
    python setup.py install
    
Once installed, `ellipcorr` can be used in python as:

    In [1]: import ellipcorr

    In [2]: ellipcorr.ellipticity_corr('sP', 65, 124, 45, 39)
    Out[2]: -0.38976147770881653

    In [3]: ellipcorr.ellipticity_corr('P', 65, 124, 45, 39)
    Out[3]: -0.3774765431880951

    In [4]: ellipcorr.ellipticity_corr('pPKiKP', 65, 124, 45, 39)
    Out[4]: -0.7800000309944153
    
With the ellipticity corrections matching those indicated in
[ellip/ttimel.help](ellip/ttimel.help).


### Tests

To run tests:

    cd /path/to/ellip-corr/
    python setup.py test
    