read-GRACE-geocenter
====================

[![Language](https://img.shields.io/badge/python-v3.8-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/github/license/tsutterley/read-GRACE-geocenter)](https://github.com/tsutterley/geoid-toolkit/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/159227455.svg)](https://zenodo.org/badge/latestdoi/159227455)

Reads geocenter data from Sutterley et al. (2019) for updating Level-2 spherical
harmonic data from the NASA/DLR Gravity Recovery and Climate Experiment
(GRACE) and the NASA/GFZ Gravity Recovery and Climate Experiment Follow-On
(GRACE-FO) missions

![geocenter-time-series](https://tsutterley.github.io/references/Sutterley-2019bx.png)

- [Figshare Data Repository](https://doi.org/10.6084/m9.figshare.7388540)
- [NASA GRACE mission site](http://www.nasa.gov/mission_pages/Grace/index.html)
- [JPL GRACE Tellus site](http://grace.jpl.nasa.gov/)
- [JPL GRACE-FO site](https://gracefo.jpl.nasa.gov/)
- [UTCSR GRACE site](http://www.csr.utexas.edu/grace/)

#### Calling Sequence
```
from read_GRACE_geocenter import read_GRACE_geocenter
CSR_input = read_GRACE_geocenter('CSR_RL06_MPIOM_SLF_iter.txt')
```
#### Inputs
 - full path to input geocenter file

#### Outputs
 - `C10`: cosine spherical harmonics of degree one and order zero (Z-component)
 - `C11`: cosine spherical harmonics of degree one and order one (X-component)
 - `S11`: sine spherical harmonics of degree one and order one (Y-component)
 - `time`: mid-month date in year-decimal
 - `JD`:  mid-month date as Julian day
 - `month`: [GRACE month of data](https://tsutterley.github.io/data/GRACE-Months.html)
 - `header`: text header of the geocenter file (will parse YAML headers)

#### Dependencies
 - [numpy: Scientific Computing Tools For Python](https://numpy.org)
 - [PyYAML: YAML parser and emitter for Python](https://github.com/yaml/pyyaml)

#### Data Description

- *Release-5 Geocenter Coefficients:*
    Derived from GRACE mission measurements and OMCT ocean model outputs.
    Represents the largest-scale variability of hydrologic, cryospheric, and solid
    Earth processes as well as the atmospheric and oceanic processes not captured
    in the GRACE RL05 de-aliasing product.  Glacial Isostatic Adjustment (GIA)
    estimates from A et al. (2013) have been restored.  ECMWF corrections from
    Fagiolini et al. (2015) have been restored.

- *Release-5 Geocenter Coefficients with Atmospheric and Oceanic Variability:*
    Derived from GRACE mission measurements and OMCT ocean model outputs.
    Represents the largest-scale variability of atmospheric, oceanic, hydrologic,
    cryospheric, and solid Earth processes.  Glacial Isostatic Adjustment (GIA)
    estimates from A et al. (2013) have been restored.  Monthly estimates of
    atmospheric and oceanic variability from the GRACE RL05 de-aliasing product
    (GAC) have been restored.

- *Release-6 Geocenter Coefficients:*
    Derived from GRACE mission measurements and MPIOM ocean model outputs.
    Represents the largest-scale variability of hydrologic, cryospheric, and solid
    Earth processes as well as the atmospheric and oceanic processes not captured
    in the GRACE RL06 de-aliasing product.  Glacial Isostatic Adjustment (GIA)
    estimates from A et al. (2013) have been restored.

- *Release-6 Geocenter Coefficients with Atmospheric and Oceanic Variability:*
    Derived from GRACE mission measurements and MPIOM ocean model outputs.
    Represents the largest-scale variability of atmospheric, oceanic, hydrologic,
    cryospheric, and solid Earth processes.  Glacial Isostatic Adjustment (GIA)
    estimates from A et al. (2013) have been restored.  Monthly estimates of
    atmospheric and oceanic variability from the GRACE RL06 de-aliasing product
    (GAC) have been restored.

#### References
T. C. Sutterley, and I. Velicogna, "Improved estimates of geocenter variability
from time-variable gravity and ocean model outputs", *Remote Sensing*,
11(18), 2108, (2019). [doi:10.3390/rs11182108](https://doi.org/10.3390/rs11182108)

S. C. Swenson, D. P. Chambers, and J. Wahr, "Estimating geocenter variations
from a combination of GRACE and ocean model output", *Journal of Geophysical
Research: Solid Earth*, 113(B08410), (2008).
[doi:10.1029/2007JB005338](https://doi.org/10.1029/2007JB005338)

G. A, J. Wahr, and S. Zhong, "Computations of the viscoelastic response of a
3-D compressible Earth to surface loading: an application to Glacial Isostatic
Adjustment in Antarctica and Canada", *Geophysical Journal International*,
192(2), 557-572, (2013). [doi:10.1093/gji/ggs030](https://doi.org/10.1093/gji/ggs030)

E. Fagiolini, F. Flechtner, M. Horwath, H. Dobslaw, "Correction of
inconsistencies in ECMWF's operational analysis data during de-aliasing of
GRACE gravity models", *Geophysical Journal International*, 202(3), 2150,
(2015). [doi:10.1093/gji/ggv276](https://doi.org/10.1093/gji/ggv276)

#### Data Repository
T. C. Sutterley and I. Velicogna, "Geocenter Estimates from Time-Variable
Gravity and Ocean Model Outputs", (2019).
[doi:10.6084/m9.figshare.7388540](https://doi.org/10.6084/m9.figshare.7388540)

#### Download
The program homepage is:  
https://github.com/tsutterley/read-GRACE-geocenter  
A zip archive of the latest version is available directly at:  
https://github.com/tsutterley/read-GRACE-geocenter/archive/main.zip  

#### Disclaimer
This program is not sponsored or maintained by the Universities Space Research
Association (USRA) or NASA.  It is provided here for your convenience but
_with no guarantees whatsoever_.

#### License
The content of this project is licensed under the
[Creative Commons Attribution 4.0 Attribution license](https://creativecommons.org/licenses/by/4.0/)
and the source code is licensed under the [MIT license](LICENSE).
