# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:38:17 2020

@author: alexw
"""

string = 'aaaaaaabbbbbccccccccc'


def stringStrip(in_string, n):
    
    #Initialise out string and outer count
    out_string = ''
    outer_n = 0
    
    #Loop through input string
    while outer_n < len(in_string):
        
        #Initialise consecutive list
        consec_string = ''
        start_char = in_string[outer_n]
        inner_n = 0
        try:
            while in_string[outer_n + inner_n] == start_char:
                consec_string += in_string[outer_n + inner_n]
                inner_n += 1
        except IndexError as error:
                pass
        
        #If consecutive characters greater than or equal to consecutive character limit
        if consec_string.count(consec_string[0]) >= n:
            out_string += consec_string[:n]
            outer_n += 1 + len(consec_string)
        #If consecutive characters less than consecutive character limit
        else:
            out_string += consec_string
            outer_n += 1 + len(consec_string)
        
    return out_string
    
    
def checkEqual(list):
    
    return len(set(list)) <= 1

out_string = stringStrip(string, 1)
print(out_string)