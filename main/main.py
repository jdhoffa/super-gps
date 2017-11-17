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

''' SGP.loadData() will produce a list of N elements, with each element corresponding to one SN dataset. 
Each dataset consists of 8 columns: 
'Varlist, 'MJD', 'FLT', 'FIELD', 'FLUXCAL', 'FLUXCALERR', 'MAG', 'MAGERR' 
And a varying number of rows, corresponding to the length of the time series '''

dataset = SGP.loadData(path)

# plot random dataset
import random
random_dataset = random.choice(dataset)
random_dataset['MJD']
x = random_dataset['MJD']
y = random_dataset['MAG']
yerr = random_dataset['MAGERR']

# note: each dataset has values for different filters, not organized. have to split data by filter. first have to determine which filters are present in dataset
