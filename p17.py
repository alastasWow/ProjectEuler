# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 19:33:19 2017

@author: Refaia
"""

sum1_9 = 36
sum10_19 = 70
sum20_99 = 8 * sum1_9 + 10 * (len('twenty') + len('thirty') + len('forty')
                              + len('fifty') + len('sixty') + len('seventy')
                              + len('eighty') + len('ninety'))

sum1_99 = sum1_9 + sum10_19 + sum20_99


hundred_and = len('hundred and') - 1

hundred = len('hundred')

sum100_999 = sum1_9 * 100 + sum1_99 * 9 + hundred_and * 99 * 9 + hundred * 9

one_thousand = len('one thousand') - 1

sum1_1000 = one_thousand + sum100_999 + sum1_99
                  
print(sum1_1000) 
