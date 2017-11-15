import os
import numpy as np

def loadData(path):
    
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
