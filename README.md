read-GRACE-geocenter
====================

Reads geocenter data from Sutterley et al. (2019) for updating spherical
harmonic coefficients from the NASA/DLR Gravity Recovery and Climate Experiment
(GRACE) and the NASA/GFZ Gravity Recovery and Climate Experiment Follow-On
(GRACE-FO) missions  

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
 - [numpy: Scientific Computing Tools For Python](http://www.numpy.org)  
 - [PyYAML: YAML parser and emitter for Python](https://github.com/yaml/pyyaml)  

#### References
S. C. Swenson, D. P. Chambers, and J. Wahr, "Estimating geocenter variations
from a combination of GRACE and ocean model output", *Journal of Geophysical
Research: Solid Earth*, 113(B08410), (2008).
[doi:10.1029/2007JB005338](https://doi.org/10.1029/2007JB005338)

#### Download
The program homepage is:   
https://github.com/tsutterley/read-GRACE-geocenter   
A zip archive of the latest version is available directly at:    
https://github.com/tsutterley/read-GRACE-geocenter/archive/master.zip  

#### Disclaimer  
This program is not sponsored or maintained by the Universities Space Research Association (USRA) or NASA.  It is provided here for your convenience but _with no guarantees whatsoever_.  
