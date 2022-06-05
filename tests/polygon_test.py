# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 23:47:11 2022

@author: Huihui
"""
import unittest

from Polygon_forex import AUDUSD_return
#from Polygon import GBPEUR_return
#from Polygon import USDCAD_return

class PolygonTestCase(unittest.TestCase):
    
   
    def test_float_number(self):
        
        self.A = AUDUSD_return(tick_time="2022-06-04 10:39:06",avg_price=1)
        self.A.last_price = 10
        self.A.hist_return = 100
        self.A.run_sum = 100
        self.A.num = 10
        result = self.A.get_avg(pop_value=1.5)
        self.assertEqual(result, 9.85)
    def test_integer_number(self):
        self.A = AUDUSD_return(tick_time="2022-06-04 10:39:06",avg_price=1)
        self.A.last_price = 10
        self.A.hist_return = 100
        self.A.run_sum = 100
        self.A.num = 10
        result = self.A.get_avg(pop_value=1)
        self.assertEqual(result, 9.9)
    def test_zero(self):
         self.A = AUDUSD_return(tick_time="2022-06-04 10:39:06",avg_price=1)
         self.A.last_price = 10
         self.A.hist_return = 100
         self.A.run_sum = 100
         self.A.num = 10
         result = self.A.get_avg(pop_value=0)
         self.assertEqual(result, 10.0)
                 
if __name__ == '__main__':
    unittest.main()