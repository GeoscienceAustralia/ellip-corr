## ak135 Travel Time Ellipticity Correction

This repo was started from ftp://rses.anu.edu.au/pub/ak135/.

We simply exposed a python shared object for `ak135` travel time ellipticity 
correction. 

### How to use

After cloning the repo
    
    cd tau && make all
    cd ../ellip && make all
    
This will create a shared object `ellip/ellipcorr.so`, which can be imported 
and used in python as:

    import ellopcorr
    ellipcorr.ellipticity_corr('sP', 65, 124, 45, 39)
    ellipcorr.ellipticity_corr('P', 65, 124, 45, 39)  
