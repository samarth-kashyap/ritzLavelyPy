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
* Create the local environment and install the package with `uv`
```
uv sync --dev
```  
* Start using ritzLavelyPy from the managed environment.

``` bash
uv run python
```

### Running tests

``` bash
uv run pytest
```


### Using the package

```python
from ritzLavelyPy.rlclass import ritzLavelyPoly
import numpy as np

ell, jmax = 100, 5 #defining ell and max-degree
RLP = ritzLavelyPoly(ell, jmax)

# generating Ritzwoller-Lavely polynomials
Pjl = RLP.get_Pjl() # the Ritzwoller-Lavely polynomials

# Create a sample function of m with length 2*ell + 1
m = np.arange(-ell, ell + 1)
alm = 0.5 + 0.01 * m - 2e-4 * m**3

# Decomposition of the array into Ritzwoller-Lavely polynomials
ritz_coeffs = RLP.get_coeffs(alm)

# Polynomial expansion using coefficients
alm_from_coeffs = RLP.polyval(ritz_coeffs)
```

### Citing the package
This package was created as a part of the study [Kashyap+(2021)](https://ui.adsabs.harvard.edu/abs/2021ApJS..253...47K/abstract). Please cite the paper as follows:

```
@ARTICLE{Kashyap-2021-ApJS,
       author = {{Kashyap}, Samarth G. and {Das}, Srijan Bharati and {Hanasoge}, Shravan M. and {Woodard}, Martin F. and {Tromp}, Jeroen},
        title = "{Inferring Solar Differential Rotation through Normal-mode Coupling Using Bayesian Statistics}",
      journal = {\apjs},
     keywords = {Helioseismology, Solar oscillations, Solar differential rotation, Markov chain Monte Carlo, 709, 1515, 1996, 1889, Astrophysics - Solar and Stellar Astrophysics},
         year = 2021,
        month = apr,
       volume = {253},
       number = {2},
          eid = {47},
        pages = {47},
          doi = {10.3847/1538-4365/abdf5e},
archivePrefix = {arXiv},
       eprint = {2101.08933},
 primaryClass = {astro-ph.SR},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2021ApJS..253...47K},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```
