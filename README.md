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

