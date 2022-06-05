# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 13:14:23 2022

@author: Huihui
"""

from Polygon_forex import AUDUSD_return
from Polygon_forex import GBPEUR_return
from Polygon_forex import USDCAD_return

#AUDUSD
#avg price = 1
A = AUDUSD_return(tick_time="2022-06-04 10:39:06",avg_price=1)
A.last_price = 10
A.hist_return = 100
A.run_sum = 100.0
A.num = 10
#pop price = 2

print("The average return of AUDUSD is:")
print(A.get_avg(pop_value=2.0))

#GBPEUR
#avg price = 1
B = GBPEUR_return(tick_time="2022-06-04 10:39:06",avg_price=1)
B.last_price = 10
B.hist_return = 100 
B.run_sum = 1000
B.num = 10000
#pop price = 2
print("The average return of GBPEUR is:")
print(B.get_avg(pop_value=2))

#USDCAD
#avg price = 1
C = USDCAD_return(tick_time="2022-06-04 10:39:06",avg_price=1)
C.last_price = 10
C.hist_return = 100 
C.run_sum = 10000
C.num = 10000
#pop price = 2
print("The average return of USDCAD is:")
print(C.get_avg(pop_value=2))
