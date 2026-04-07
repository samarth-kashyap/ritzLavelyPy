import numpy as np

from ritzLavelyPy.rlclass import ritzLavelyPoly


def test_get_pjl_shape_and_leading_terms():
    poly = ritzLavelyPoly(ell=4, jmax=3)

    assert poly.Pjl.shape == (4, 9)
    np.testing.assert_allclose(poly.Pjl[0], np.full(9, 4.0))
    np.testing.assert_allclose(poly.Pjl[1], np.arange(-4, 5, dtype=float))


def test_coeff_round_trip_reconstructs_signal():
    poly = ritzLavelyPoly(ell=25, jmax=6)
    coeffs = np.array([1.2, -0.5, 0.3, 0.0, -0.1, 0.05, 0.02])

    signal = poly.polyval(coeffs)
    recovered = poly.get_coeffs(signal)

    np.testing.assert_allclose(recovered, coeffs, rtol=1e-10, atol=1e-10)


def test_invalid_lengths_raise_assertion():
    poly = ritzLavelyPoly(ell=5, jmax=2)

    try:
        poly.get_coeffs(np.ones(3))
    except AssertionError as exc:
        assert "Length of input array" in str(exc)
    else:
        raise AssertionError("Expected get_coeffs to reject invalid input length")

    try:
        poly.polyval(np.ones(2))
    except AssertionError as exc:
        assert "Number of coeffs" in str(exc)
    else:
        raise AssertionError("Expected polyval to reject invalid coefficient length")
