"""Module to handle decomposition of functions in terms of 
Ritzwoller-Lavely polynomials (Ritzwoller & Lavely, 1991) and
reconstruction of functions from the Ritzwoller-Lavely coefficients.
"""
import numpy as np
import scipy.special as special
import numpy.polynomial.legendre as npleg

NAX = np.newaxis

class ritzLavelyPoly():
    """Class to handle Ritzwoller-Lavely polynomials and coefficients.

    Attributes:
    ------------
        ell - int
            The spherical harmonic degree

        jmax - int
            The maximum order of polynomial

        m - np.ndarray(ndim=1, dtype=int)
            Array containing azimuthal order (-ell, -ell+1, ..., ell-1, ell)

        L - float
            sqrt(ell*(ell+1))

        m_by_L - np.ndarray(ndim=1, dtype=float)
            m/L

        Pjl - np.ndarray(ndim=1, dtype=float)
            Ritzwoller-Lavely polynomials
            axis=0 : polynomial order
            axis=1 : azimuthal order m

        Pjl_exists - bool
            flag to check if polynomials are already computed

    Methods:
    ---------
        get_Pjl - computes Ritzwoller-Lavely polynomials
        get_coeffs - computes Ritzwoller-Lavely coefficients of a given function
        polyval - uses Ritzwoller-Lavely coefficients to compute the function
    """
    def __init__(self, ell, jmax):
        """ Class instance initializer """
        assert ell > 0, "Ritzwoller-Lavely polynomials don't exist for ell=0"
        assert jmax + 1 <= 2*ell, "Max degree (jmax) should be smaller than 2*ell"
        self.ell = ell
        self.jmax = jmax + 1
        self.m = np.arange(-ell, ell+1) * 1.0
        self.L = np.sqrt(ell*(ell+1))
        self.m_by_L = self.m/self.L
        self.Pjl = np.zeros((self.jmax, len(self.m)), dtype=np.float64)
        print(f"Generating the Ritzwoller-Lavely polynomials for " +
              f"ell = {ell} and jmax = {jmax}")
        self.get_Pjl()

    def get_Pjl(self):
        """Computes the Ritzwoller-Lavely polynomials for given ell and jmax"""
        self.Pjl[0, :] += self.ell
        self.Pjl[1, :] += self.m
        for j in range(2, self.jmax):
            coeffs = np.zeros(j+1)
            coeffs[-1] = 1.0
            P2j = self.L * npleg.legval(self.m_by_L, coeffs)
            cj = self.Pjl[:j, :] @ P2j / (self.Pjl[:j, :]**2).sum(axis=1)
            P1j = P2j - (cj[:, NAX] * self.Pjl[:j, :]).sum(axis=0)
            self.Pjl[j, :] += self.ell * P1j/P1j[-1]
        return self.Pjl

    def get_coeffs(self, arrm):
        """Decomposition of input array into Ritzwoller-Lavely coefficients.

        Inputs:
        -------
        arrm - np.ndarray(ndim=1, dtype=float)
            array that needs to be decomposed

        Returns:
        --------
        aj - np.ndarray(ndim=1, dtype=float)
            Ritzwoller-Lavely coefficients
        """
        assert len(arrm) == len(self.m), "Length of input array =/= 2*ell+1"
        aj = (self.Pjl @ arrm) / np.diag(self.Pjl @ self.Pjl.T)
        return aj

    def polyval(self, acoeffs):
        """Reconstruction of function from the Ritzwoller-Lavely coefficients.

        Inputs:
        -------
        acoeffs - np.ndarray(ndim=1, dtype=float)
            the array containing Ritzwoller-Lavely coefficients

        Returns:
        --------
        sum(acoeffs * Pjl) - np.ndarray(ndim=1, dtype=float)
            the reconstructed function
        """
        assert len(acoeffs) == self.jmax, (f"Number of coeffs ({len(acoeffs)} " +
                                           f"=/= jmax ({self.jmax})")
        return (acoeffs[:, NAX] * self.Pjl).sum(axis=0)
