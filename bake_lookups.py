# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 10:46:34 2016

@author: Mike
"""
from ONSdatabaker.constants import *

def per_file(tabs):
    
    return ["*"]
    
    
def per_tab(tab):

    # if its a data tab,we dont want it    
    if tab.name == 'Data':
        return    

    starting_point = tab.excel_ref('A').filter(contains_string('Hierarchy')).shift(RIGHT).expand(DOWN)

    # Get the CDID translations      
    obs = starting_point.fill(DOWN).is_not_blank().is_not_whitespace()
   
    tab.dimension("Holding Value", "Doesnt Matter")        

    yield obs