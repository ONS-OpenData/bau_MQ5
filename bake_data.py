# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 10:46:34 2016

@author: Mike
"""
from __future__ import unicode_literals
from ONSdatabaker.constants import *

def per_file(tabs):
    
    return ["Data"]
    
    
def per_tab(tab):
      
    obs = tab.excel_ref('C2').expand(RIGHT).expand(DOWN).is_not_blank().is_not_whitespace()
    
    tab.excel_ref('C1').expand(RIGHT).is_not_blank().is_not_whitespace().dimension(TIME, DIRECTLY, ABOVE)
   
    tab.excel_ref('A2').expand(DOWN).is_not_blank().is_not_whitespace().dimension('Institutional Group', DIRECTLY, LEFT)        

    tab.excel_ref('B2').expand(DOWN).is_not_blank().is_not_whitespace().dimension(PARAMS(0), DIRECTLY, LEFT) 

    yield obs