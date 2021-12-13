## ritzLavelyPy
A package to handle Ritzwoller-Lavely polynomials [(Ritzwoller & Lavely, 1991)](https://ui.adsabs.harvard.edu/abs/1991ApJ...369..557R/abstract)
used to represent helioseismic split frequencies using a-coefficients.

Documentation can be found here. [(link)](https://samarth-kashyap.github.io/ritzLavelyPy/)

### Installing the package
* Clone the repository ritzLavelyPy into local working directory.
``` bash
cd /local/working/dir/
git clone https://github.com/samarth-kashyap/ritzLavelyPy.git
```
* Enter the cloned directory

``` bash
cd /local/working/dir/ritzLavelyPy
```
* Install the python package
```
pip install -e .
```  
* Start using ritzLavelyPy.


### Using the package

```python
from ritzLavelyPy import ritzLavelyPoly
ell, jmax = 100, 5 #defining ell and max-degree
RLP = ritzLavelyPoly(ell, jmax)

# generating Ritzwoller-Lavely polynomials
Pjl = RLP.get_Pjl() # the Ritzwoller-Lavely polynomials

# Decomposition of the given array (function of m)
# into Ritzwoller-Lavely polynomials
alm = np.load('alm.npy')
ritz_coeffs = RLP.get_coeffs(alm)

# Polynomial expansion using coefficients
alm_from_coeffs = RLP.polyval(ritz_coeffs)
```

