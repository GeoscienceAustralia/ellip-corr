from __future__ import print_function
import pytest
from ellip import ellipcorr

data = "1  P          626.67     626.29     6.4671  -1.09E-01  -4.25E-03 \
           2  pP         656.86     656.44     6.5478   1.09E-01  -4.21E-03 \
           3  PcP        658.64     658.24     4.1323  -1.18E-01   1.38E-02 \
           4  sP         670.33     669.94     6.5283   2.14E-01  -4.23E-03 \
           5  PP         771.08     770.21     8.7483  -9.46E-02  -1.25E-02 \
           6  PKiKP     1023.14    1022.39     1.3232  -1.23E-01   1.85E-02 \
           7  pPKiKP    1056.64    1055.86     1.3198   1.23E-01   1.85E-02 \
           8  sPKiKP    1069.35    1068.57     1.3205   2.22E-01   1.85E-02 \
           9  S         1138.79    1138.09    12.2313  -1.92E-01  -2.71E-03 \
          10  SPn       1156.30    1155.24    13.6603  -1.83E-01  -2.31E-02 \
          11  pS        1173.59    1172.86    12.5499   4.63E-02  -2.35E-03 \
          12  PnS       1176.56    1175.52    13.3906  -1.75E-02  -5.56E-03 \
          13  sS        1190.77    1189.99    12.3694   1.91E-01  -2.67E-03 \
          14  SKSac     1209.68    1208.96     7.5880  -2.11E-01  -1.13E-01 \
          15  SKKSac    1209.69    1208.96     7.5903  -2.11E-01  -4.81E-01 \
          16  ScS       1209.82    1209.09     7.6990  -2.11E-01   7.04E-03 \
          17  SKiKP     1224.71    1223.85     1.3785  -2.22E-01   1.83E-02 \
          18  pSKSac    1252.33    1251.52     7.5901   1.03E-01  -2.07E-01 \
          19  sSKSac    1266.12    1265.32     7.5896   2.11E-01  -1.63E-01 \
          20  SS        1392.86    1391.30    15.5487  -1.70E-01  -9.16E-03 \
          21  PKKPdf    1850.64    1847.18    -1.3739  -1.23E-01  -1.69E-02 \
          22  SKKPdf    2052.18    2047.84    -1.3144  -2.22E-01  -1.71E-02 \
          23  PKKSdf    2064.89    2059.97    -1.3136  -1.23E-01  -1.71E-02 \
          24  SKKSdf    2266.24    2260.25    -1.2580  -2.22E-01  -1.75E-02 \
          25  P'P'df    2350.14    2351.31    -1.6599  -1.23E-01  -2.16E-02 \
          26  P'P'bc    2355.43    2356.61    -2.7297  -1.21E-01  -3.67E-03 \
          27  P'P'ab    2359.80    2360.97    -3.9679  -1.19E-01   7.93E-03 \
          28  S'S'df    3197.06    3195.36    -1.3915  -2.22E-01  -1.70E-02"

data = data.split()

ellipcorr_dict = {}

for i, d in enumerate(data):
    if i % 7 == 1:
        k = d
    if i % 7 == 2:
        tt = float(d)
    if i % 7 == 3:
        tcor = float(d) - tt
        ellipcorr_dict[k] = tcor


@pytest.fixture(params=list(ellipcorr_dict.keys()))
def phase_corr(request):
    return request.param, ellipcorr_dict[request.param]


def test_ellipticity_corr(phase_corr):
    phase, corr = phase_corr
    ell_corr = ellipcorr.ellipticity_corr(phase, 65, 124, 45, 39)
    assert abs(ell_corr - corr) < 1.0e-2
