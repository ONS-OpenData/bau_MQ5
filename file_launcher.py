# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:02:46 2016

@author: Mike

Simple python script launcher
"""

import pandas as pd
import subprocess as sp
import os
import compare as cp
import validation_tool as vt


""" QUARTER COUNT
each MQ5 dataset deals with X  number of quarters, we need to pass this in manually.
literally, just a count of the columns of observations we are extracting.
"""
print ''
print '----------------------------'
print ' MQ5 Transformation Scripts '
print '----------------------------'
print ''
quarter_count = raw_input('Please input the number of columns to be extracted... ')
quarter_count = int(quarter_count)

# Get all .xls and .xlsx fiels from the current working directory
files = [x for x in os.listdir('.') if os.path.isfile(x)]
files = [x for x in files if '.xls' in x or '.xlsx' in x]

# And make sure we dont count preview excels
files = [x for x in files if 'preview' not in x]

for f in files:
    """
    For each file do the following:
    1.) Databake the lookup info into something we can use
    2.) Write the "lookup" data into a file
    """
    
    # Get the lookup info
    p = sp.Popen('bake --preview bake_lookups.py "' + f + '"', shell=True)
    p.communicate()


    # Get the contents for dim_id_1 from the file name
    if 'QNI' in f: myArg = 'Label'
    if 'QAD' in f: myArg = 'Transactions in financial assets'
    if 'QH' in f: myArg = 'Financial instrument'

    # Databake the data tab
    p = sp.Popen('bake --preview bake_data.py "' + f + '" ' + myArg, shell=True)
    p.communicate()


# Gather all the files starting with data, NOT the lookup ones
files = [x for x in os.listdir('.') if os.path.isfile(x)]
files = [x for x in files if 'data-' in x and '.csv' in x and 'bake_lookups' not in x and 'transform-' not in x]


for f in files:
    """
    For each "data-" file do the following
    1.) Write the "lookup" information into the file
    
    NOTE - we cant do a typical lookup as the tale is full of N/A's, so youd be calling
    1 of about 50 possible results each time.
    
    Instead. The file as extracted always follows a repeating pattern of 1 per quarter of data of each
    item. We'll just iterate this pattern in.
    """

    # Load data file    
    obs_file = pd.read_csv(f, dtype=object)
    
    # Get lookup file
    f_split = f.split('bake_data')
    f2 = f_split[0] + 'bake_lookups-.csv'
    lookup_file = pd.read_csv(f2, dtype=object)    
    
    # Stack a list full of items we want    
    lookup_items = ()
    for i, row in lookup_file[:-1].iterrows():
        addme = (lookup_file.ix[i, 'data_marking'],)
        lookup_items = lookup_items + addme
        
    # Iterate the obs file, each lookup_item filling x consecative rows
    obs_file = pd.read_csv(f, dtype=object)
    count = 0   
    for i, row in obs_file[:-1].iterrows():
        which_one = count / quarter_count
        if which_one == len(lookup_items):
            count = 0
            which_one = 0
        obs_file.ix[i, 'dim_item_id_2'] = lookup_items[which_one]
        count +=1
        
    obs_file['dimension_item_label_eng_2'] = obs_file['dim_item_id_2']       
        
    # Outout tranformed file
    newname = 'transform-' + f[5:]
    obs_file.to_csv(newname, index=False)
    
    
    """ validation and dimension comparisson """
    vt.frame_checks(obs_file, newname)
    if 'MQ5QAD' in newname:
        cp.compare('MQ5QAD', newname) 
    if 'MQ5QH' in newname:
        cp.compare('MQ5QH', newname) 
    if 'MQ5QNI' in newname:
        cp.compare('MQ5QNI', newname)
        
        

    
    

    


    
    
