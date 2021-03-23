import rlclass as RLC
import numpy as np
import matplotlib.pyplot as plt

ell = 150
L = np.sqrt(ell*(ell+1))
m_arr = np.arange(-ell, ell+1)
mbl = m_arr/L
rlp = RLC.ritzLavelyPoly(ell, 36)
freqs = mbl*430 + (mbl**3)*(21.5) + (mbl**5)*(-6.7) + (mbl**2)*(7e-6) + (mbl**4)*(9e-12)
rlp.get_Pjl()
acoeffs = rlp.get_coeffs(freqs)
print(acoeffs)
freqs2 = rlp.polyval(acoeffs)
plt.plot(m_arr, freqs, 'r')
plt.plot(m_arr, freqs2, '--b')
plt.show()
