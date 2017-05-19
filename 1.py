#!/usr/bin/evn python3
#-*- coding:utf-8 -*-
def xx(x=1,y=1):
    z=x*y
    while(x<=9):
        if(y<=9):
            print('%d*%d=%d' %(x,y,z))
            return xx(x,y+1)
        else:
            return xx(x+1,x+1)
