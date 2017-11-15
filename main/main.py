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

''' load and tidy data '''

# path to dataset
path = '../data/'
# lcs or photo?
ext = 'lightcurves/'
# ext = 'photometry'

# sample dataset
sample = 'SN2000fa.txt'

'''load all datasets into single numpy array'''
temp_list = []

for filename in os.listdir(path+ext):
    if filename.endswith('.txt'):
        with open(path+ext+filename, 'r') as f:
            content = f.readlines()

            # strip \n characters
            content = [x.strip() for x in content]

            # determine length of header
            for i in range(0,len(content)):
                if content[i][0:5] == 'OBS: ':
                    header_length = i
                    break
            
            # determine length of footer
            for j in range(0,len(content)):
                if content[j][0:4] == 'END:':
                    footer_length = len(content) - j
                    break

            data = np.genfromdata = np.genfromtxt(path+ext+filename, dtype=None, skip_header=header_length, \
                     skip_footer = footer_length, \
                     names= ('VARLIST', 'MJD', 'FLT','FIELD', 'FLUXCAL', 'FLUXCALERR', \
                             'MAG', 'MAGERR')) # photometry data

            temp_list.append(data)
