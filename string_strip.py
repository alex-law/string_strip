# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:38:17 2020

@author: alexw
"""

string = 'aabbbbbccc'


def stringStrip(in_string, consec_chars):
    
    #Initialise out string and outer count
    out_string = ''
    outer_n = 0
    
    #Loop through input string
    while outer_n < len(in_string):
        
        #Initialise consecutive list
        consec_char = ''
        start_char = in_string[outer_n]
        inner_n = 0
        while in_string[inner_n] == start_char:
            try:
                consec_char += in_string[outer_n + inner_n]
                inner_n += 1
            except IndexError as error:
                pass
        
        
        #If consecutive characters match consecutive character limit
        if consec_char.count(consec_char[0]) == len(consec_char):
            out_string += consec_char
            outer_n += 1 + consec_chars
        #If consecutive characters gretaer than consecutive character limit
        elif consec_char.count(consec_char[0]) > len(consec_char):
            out_string += consec_char[:consec_char]
            outer_n += 1 + consec_chars
        #If consecutive characters less than consecutive character limit
        else:
            out_string += consec_char
            outer_n += 1 + consec_chars
        
    return out_string
    
    
def checkEqual(list):
    
    return len(set(list)) <= 1

out_string = stringStrip(string, 2)
print(out_string)