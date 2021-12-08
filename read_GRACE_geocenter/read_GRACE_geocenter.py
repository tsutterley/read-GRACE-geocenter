#!/usr/bin/env python
u"""
read_GRACE_geocenter.py
Written by Tyler Sutterley (12/2021)
Reads geocenter file and extracts dates and spherical harmonic data

INPUTS:
    input_file: input datafile with geocenter coefficients

OUTPUTS:
    C10: Cosine degree one/order zero harmonics (Z-component)
    C11: Cosine degree one/order one harmonics (X-component)
    S11: Sine degree one/order one harmonics (Y-component)
    time: mid-month date of range in year-decimal
    JD: mid-month date of range as Julian day
    month: GRACE/GRACE-FO month (months starting 2002-01: 2002-04 = 004)

PYTHON DEPENDENCIES:
    numpy: Scientific Computing Tools For Python
        http://www.numpy.org
    PyYAML: YAML parser and emitter for Python
        https://github.com/yaml/pyyaml

REFERENCES:
    T. C. Sutterley, and I. Velicogna, "Improved estimates of geocenter
        variability from time-variable gravity and ocean model outputs,
        Remote Sensing, 11(18), 2108, (2019).
        doi:10.3390/rs11182108

    S. C. Swenson, D. P. Chambers, and J. Wahr, "Estimating geocenter variations
        from a combination of GRACE and ocean model output",
        Journal of Geophysical Research: Solid Earth, 113(B08410), (2008).
        doi:10.1029/2007JB005338

UPDATE HISTORY:
    Updated 12/2021: use YAML header to extract data column indices
    Updated 11/2021: define int/float precision to prevent deprecation warning
    Updated 07/2020: added function docstrings
    Written 11/2018 for public release
"""
import os
import re
import copy
import yaml
import numpy as np

#-- PURPOSE: read degree one spherical harmonic data
def read_GRACE_geocenter(input_file):
    """
    Reads monthly geocenter files computed using
    GRACE/GRACE-FO measurements and ocean models

    Arguments
    ---------
    input_file: input datafile with geocenter coefficients

    Returns
    -------
    C10: Cosine degree one/order zero spherical harmonics
    C11: Cosine degree one/order one spherical harmonics
    S11: Sine degree one/order one spherical harmonics
    time: mid-month date of range in year-decimal
    JD: mid-month date of range as Julian day
    month: GRACE/GRACE-FO month
    """

    #-- read geocenter file and get contents
    with open(os.path.expanduser(input_file),'r') as f:
        file_contents = f.read().splitlines()
    #-- number of lines contained in the file
    file_lines = len(file_contents)

    #-- counts the number of lines in the header
    HEADER = False
    count = 0
    #-- Reading over header text
    while (HEADER is False) and (count < file_lines):
        #-- file line at count
        line = file_contents[count]
        #--if End of YAML Header is found: set HEADER flag
        HEADER = bool(re.search("\# End of YAML header",line))
        #-- add 1 to counter
        count += 1

    #-- verify HEADER flag was set
    if not HEADER:
        raise IOError('Data not found in file:\n\t{0}'.format(input_file))

    #-- number of months within the file
    n_mon = np.int64(file_lines - count)
    #-- output time variables
    grace_input = {}
    grace_input['time'] = np.zeros((n_mon))
    grace_input['JD'] = np.zeros((n_mon))
    grace_input['month'] = np.zeros((n_mon), dtype=np.int64)
    #-- parse the YAML header (specifying yaml loader)
    grace_input.update(yaml.load('\n'.join(file_contents[:count]),
        Loader=yaml.BaseLoader))

    #-- compile numerical expression operator
    regex_pattern = '[-+]?(?:(?:\d*\.\d+)|(?:\d+\.?))(?:[Ee][+-]?\d+)?'
    rx = re.compile(regex_pattern, re.VERBOSE)

    #-- get names and columns of input variables
    variables = copy.copy(grace_input['header']['variables'])
    variables.pop('mid-epoch_time')
    variables.pop('month')
    columns = {}
    #-- for each output data variable
    for key in variables:
        grace_input[key] = np.zeros((n_mon))
        comment_text, = rx.findall(variables[key]['comment'])
        columns[key] = int(comment_text) - 1

    #-- for every other line:
    for t, line in enumerate(file_contents[count:]):
        #-- find numerical instances in line including integers, exponents,
        #-- decimal points and negatives
        line_contents = rx.findall(line)

        #-- extacting mid-date time and GRACE/GRACE-FO "month"
        grace_input['time'][t] = np.float64(line_contents[0])
        grace_input['month'][t] = np.int64(line_contents[-1])

        #-- calculate mid-date as Julian dates
        #-- calendar year of date
        year = np.floor(grace_input['time'][t])
        #-- check if year is a leap year
        days_per_year = 366.0 if ((year % 4) == 0) else 365.0
        #-- calculation of day of the year
        day_of_the_year = days_per_year*(grace_input['time'][t] % 1)
        #-- calculate JD
        grace_input['JD'][t] = np.float64(367.0*year - np.floor(7.0*(year)/4.0) -
            np.floor(3.0*(np.floor((year - 8.0/7.0)/100.0) + 1.0)/4.0) +
            np.floor(275.0/9.0) + day_of_the_year + 1721028.5)

        #-- extract fully-normalized degree one spherical harmonics
        for key,val in columns.items():
            grace_input[key][t] = np.float64(line_contents[val])

    #-- return the geocenter data, GRACE date (mid-month in decimal and in JD),
    #-- and the equivalent GRACE "month"
    return grace_input
