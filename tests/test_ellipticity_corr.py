from __future__ import print_function
import pytest
from PyEllipCorr import PyEllipCorr

"""
Source latitude:  -30
Source depth (km):  124
Azimuth from source:  39
delta: 65
           # code       time    time(el)    dT/dD     dT/dh      d2T/dD2
"""

data= """  1  P          626.6652   626.8218     6.4671  -1.09E-01  -4.26E-03
           2  pP         656.8627   657.0470     6.5478   1.09E-01  -4.21E-03
           3  PcP        658.6354   658.7878     4.1323  -1.18E-01   1.38E-02
           4  sP         670.3326   670.4863     6.5283   2.14E-01  -4.23E-03
           5  PP         771.0760   771.6174     8.7483  -9.46E-02  -1.25E-02
           6  PKiKP     1023.1398  1023.5211     1.3232  -1.23E-01   1.85E-02
           7  pPKiKP    1056.6406  1057.0413     1.3198   1.23E-01   1.85E-02
           8  sPKiKP    1069.3484  1069.7469     1.3205   2.22E-01   1.85E-02
           9  S         1138.7920  1139.0929    12.2313  -1.92E-01  -2.71E-03
          10  SPn       1156.3033  1156.9156    13.6603  -1.83E-01  -2.31E-02
          11  pS        1173.5881  1173.9027    12.5499   4.63E-02  -2.35E-03
          12  PnS       1176.5562  1177.1404    13.3906  -1.75E-02  -5.56E-03
          13  sS        1190.7726  1191.1244    12.3694   1.91E-01  -2.67E-03
          14  SKSac     1209.6849  1209.9666     7.5880  -2.11E-01  -1.13E-01
          15  SKKSac    1209.6868  1209.9685     7.5903  -2.11E-01  -4.81E-01
          16  ScS       1209.8174  1210.1000     7.6990  -2.11E-01   7.04E-03
          17  SKiKP     1224.7056  1225.1292     1.3785  -2.22E-01   1.83E-02
          18  pSKSac    1252.3256  1252.6616     7.5901   1.03E-01  -2.07E-01
          19  sSKSac    1266.1160  1266.4423     7.5896   2.11E-01  -1.63E-01
          20  SS        1392.8646  1393.8425    15.5487  -1.70E-01  -9.15E-03
          21  PKKPdf    1850.6364  1853.4150    -1.3739  -1.23E-01  -1.69E-02
          22  SKKPdf    2052.1799  2055.6609    -1.3144  -2.22E-01  -1.71E-02
          23  PKKSdf    2064.8875  2068.9170    -1.3136  -1.23E-01  -1.71E-02
          24  SKKSdf    2266.2419  2271.1333    -1.2580  -2.22E-01  -1.75E-02
          25  P'P'df    2350.1360  2348.5884    -1.6599  -1.23E-01  -2.16E-02
          26  P'P'bc    2355.4346  2353.8870    -2.7297  -1.21E-01  -3.67E-03
          27  P'P'ab    2359.7952  2358.2476    -3.9679  -1.19E-01   7.92E-03
          28  S'S'df    3197.0603  3197.8882    -1.3915  -2.22E-01  -1.70E-02"""

data = data.split()

ellipcorr_dict = {}
pyellip = PyEllipCorr()

for i, d in enumerate(data):
    if i % 7 == 1:
        k = d
    if i % 7 == 2:
        tt = float(d)
    if i % 7 == 3:
        tcor = float(d) - tt
        ellipcorr_dict[k] = tcor


@pytest.fixture(params=list(ellipcorr_dict.keys()))
def tcor_pair(request):
    return request.param, ellipcorr_dict[request.param]

def test_ellipticity_corr(tcor_pair):
    phase, corr = tcor_pair
    result = pyellip.get_correction(phase, 65, 124, (90 - -30), 39)
    print(result, corr)
    assert abs(result - corr) < 1.0e-3
