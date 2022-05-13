# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def a(t=1):
    y=0
    z=1
    for x in range(1,t+1):
        y+=x
        z*=x
    return(y,z)

while (True):
    s=input(':')
    if s=='end':
        break
    else:
        try:
            x,y=a(int(s))
            print(x,y)
        except:
            print('不是正整數')