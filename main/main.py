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

import random

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

# note: each dataset has values for different filters, not organized. have to split data by filter. first have to determine which filters are present in dataset
# here we will generate a list of all filters present in a given dataset

flt_set = []

# create an ordered list containing all filters present in each dataset
for data in dataset:
    flt_set.append(np.array(SGP.listFilters(data)))

# load random dataset
choice = random.choice(range(len(dataset)))
random_dataset = dataset[choice]
flts = flt_set[choice]
flt1 = flts[0]
x = []
y = []
yerr = []

for i in range(0,len(random_dataset['FLT'])):
    if random_dataset['FLT'][i]==flts[0]:
        x.append(random_dataset['MJD'][i])
        y.append(random_dataset['MAG'][i])
        yerr.append(random_dataset['MAGERR'][i])

plt.figure()
plt.errorbar(x,yerr,y)
plt.show()
