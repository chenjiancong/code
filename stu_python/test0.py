#!/usr/bin/env python
# encoding: utf-8

def func(a, *pargs):
    print(a,pargs)

func(1,2,3)

def func1(a,**kargs):
    print(a,kargs)

func1(a=1,c=3,b=2)

