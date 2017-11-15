# Authors:
# Jackson Hoffart <jackson dot hoffart at gmail dot com>

# License: GPL-3.0

# include this when deploying!
# ! pip freeze > requirements.txt

''' import some cheeky modules '''

# standard modules
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# optimization module
import scipy.optimize as op

# gaussian process library by DFM
import george
from george import kernels

# super GP modules
import superGPmods as SGP

''' load and tidy data '''
# path to dataset
prefix = '../data/'
# lcs or photo?
ext = 'lightcurves/'
# ext = 'photometry'

path = prefix + ext

'''load all datasets into single numpy array'''
# this will produce a nested python list of all SNe .txt files.
# each element of the list is a numpy array

dataset = SGP.loadData(path)

print(dataset[0][0])

# now len(dataset) = N, for N SNe lightcurve datasets
# each element has 8 columns: 
# 'VARLIST', 'MJD', 'FLT', 'FIELD', 'FLUXCAL', 'FLUXCALERR', 'MAG', 'MAGERR'
# e.g. dataset[1]['MJD'] will display the modified julian date values for the 2nd SN dataset


