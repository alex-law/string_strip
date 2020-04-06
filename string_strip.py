# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:38:17 2020

@author: alexw
"""

string = 'aabbccc'


def stringStrip(in_string, consec_chars):
    
    out_string = ''
    outer_n = 0
    while outer_n < len(string):
        
        consec_list = []
        if outer_n + consec_chars < len(string):
            for inner_n in range(consec_chars):    
                consec_list.append(in_string[outer_n + inner_n])
        else:
            consec_list.append(in_string[outer_n])
            
        out_string += consec_list[0]
        
        if checkEqual(consec_list):    
            outer_n += 1 + consec_chars
        else:
            outer_n += 1
        
    return out_string
    
    
def checkEqual(list):
    
    return len(set(list)) <= 1

out_string = stringStrip(string, 3)
print(out_string)