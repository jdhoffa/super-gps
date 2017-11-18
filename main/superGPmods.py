import os
import numpy as np

def loadData(path):
    ''' 
        load all .txt files from a given path as a list of numpy arrays.
        each numpy array corresponds to a single supernova dataset. 
        note: header and footer information is lost!
    '''    
    dataset = []    

    for filename in os.listdir(path):
        if filename.endswith('.txt'):
            with open(path+filename, 'r') as f:
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

                data = np.genfromdata = np.genfromtxt(path+filename, dtype=None, \
                        skip_header=header_length, \
                        skip_footer = footer_length, \
                        names= ('VARLIST', 'MJD', 'FLT','FIELD', 'FLUXCAL', 'FLUXCALERR', \
                                'MAG', 'MAGERR')) # photometry data

                dataset.append(data)
    return dataset

def listFilters(dataset):
    ''' 
        returns a list of all filters present in a given dataset
    '''
    flt_present = []
    for flt in dataset['FLT']:
        if flt in flt_present:
            continue
        else:
            flt_present.append(flt)
    return flt_present
