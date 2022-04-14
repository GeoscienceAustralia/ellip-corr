import os
from numpy import f2py
import numpy as np
from collections import defaultdict

sourcecode = open(os.path.join(os.path.dirname(__file__),'ellip/pyellip.f')).read()

f2py.compile(sourcecode, modulename='pyellip', verbose=False)
from pyellip import select_phase, coeffs, ellip

class PyEllipCorr:
    def __init__(self):
        self._tbl_fn = os.path.join(os.path.dirname(__file__), 'ellip/elcordir.tbl')
        self._coeffs = defaultdict(list)
    # end func

    def get_correction(self, phase, edist, edepth, ecolat, azim):
        """
        :param phase: a  string specifying the PHASE,   -e.g P, ScP etc.
        :param edist: epicentral distance to station (degrees)
        :param edepth: depth of event (km)
        :param ecolat: epicentral co-latitude of source (degrees)
        :param azim: azimuth from source to station (degrees)
        :return: ellipticity-correction (s)
        """

        ip, abrt = select_phase(phase, edist)
        if(abrt):
            print('Warning: Phase {} not found. Returning a null correction..'.format(phase))
            return 0
        # end if

        if ((phase, ip) not in self._coeffs.keys()):
            t0, t1, t2, d1,d2,delta, abrt = coeffs(self._tbl_fn, ip)
            if(not abrt):
                self._coeffs[(phase, ip)] = [t0, t1, t2, d1, d2, delta]
                return self.get_correction(phase, edist, edepth, ecolat, azim)
            else:
                return 0
            # end if
        else:
            ecolat_rad = np.radians(ecolat)
            azim_rad = np.radians(azim)

            t0, t1, t2, d1, d2, delta = self._coeffs[(phase, ip)]
            tcor, abrt = ellip(t0, t1, t2, d1, d2, delta, edist, edepth, ecolat_rad, azim_rad);

            if(not abrt): return tcor
            else: return 0
        # end if
    # end func
# end class

p=PyEllipCorr()