#!/usr/bin/python2.7
#-*- coding:utf-8 -*-
#Filename: hello.py

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
#    return '<h1>Hello,web!</h1>'


