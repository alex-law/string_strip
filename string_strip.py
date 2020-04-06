# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:38:17 2020

@author: alexw
"""

class StringStrip:
    """Classs strip consecutive characters in string"""
    
    def __init__(self, in_string, consec_limit):
        #Initialise variables
        self.out_string = ''
        self.outer_n = 0
        self.in_string = in_string
        self.consec_limit = consec_limit
        self.stripTheString()
        
    def stripTheString(self):
        #Loop through input string
        while self.outer_n < len(self.in_string):
            self.getConsecString()
            self.appendToOuter()
            
    def getConsecString(self):
        #Get consecutive string sections
        self.consec_string = ''
        start_char = self.in_string[self.outer_n]
        inner_n = 0
        try:
            while self.in_string[self.outer_n + inner_n] == start_char:
                self.consec_string += self.in_string[self.outer_n + inner_n]
                inner_n += 1
        except IndexError as error:
                pass

    def appendToOuter(self):
        #Append chars to output string
        #If consecutive characters equal to or greater than character limit
        #append upper limit of consecutive characters
        if self.consec_string.count(self.consec_string[0]) >= self.consec_limit:
            self.out_string += self.consec_string[:self.consec_limit]
            self.outer_n += len(self.consec_string)
        #If consecutive characters less than consecutive character limit
        #append all consecutive characters
        else:
            self.out_string += self.consec_string
            self.outer_n += len(self.consec_string)

if __name__ == '__main__':
    string = 'aaaaaaaabcdeefffff'
    strip = StringStrip(string, 2)
    print(strip.out_string)
    out_string =strip.out_string