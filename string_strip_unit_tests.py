# -*- coding: utf-8 -*-

import unittest

from string_strip import StringStrip

class TestStringStrip(unittest.TestCase):
    
    def test_getConsecString(self):
        strip = StringStrip('aabbb', 2)
        self.assertEqual(strip.consec_string, 'bbb')
        
    def test_stripTheString(self):
        strip = StringStrip('aabbbd', 2)
        self.assertEqual(strip.out_string, 'aabbd')
        strip = StringStrip('aabbbbdd', 4)
        self.assertEqual(strip.out_string, 'aabbbbdd')
        strip = StringStrip('aabbbdcccd', 2)
        self.assertEqual(strip.out_string, 'aabbdccd')
        strip = StringStrip('aabbbdeff', 1)
        self.assertEqual(strip.out_string, 'abdef')
        
if __name__ == '__main__':
    unittest.main()