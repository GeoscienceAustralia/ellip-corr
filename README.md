## ak135 Travel Time Ellipticity Correction

This repo was started from ftp://rses.anu.edu.au/pub/ak135/.

Ellipticity corrections for travel times based on `ak135`.

### Setup

    cd ellip-corr
    make

### How to use

    from PyEllipCorr import PyEllipCorr 
    p = PyEllipCorr(); 
    print(p.get_correction('P',65,124,40,39))

### Tests

To run tests:

    cd /path/to/ellip-corr/
    pytest
    
