#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: outputhtml.py

d = {'Tom':90,'Jack':78,'Merry':69,'Peter':100}

def table_data(name,score):
    return '<tr><td>%s</td></tr><tr><td>%s</td></tr>'%(name,score)

tr = ['<tr><td>%s</td></tr><tr><td>%s</td></tr>'%(name,score) for name,score in d.iteritems()]

print '<table border=1>'
print '<tr><th>Name</th></tr><tr><th>Score</th></tr>'
print '/n'.join(tr)
print '</table>'


