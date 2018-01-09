#!/usr/bin/env python
# encoding: utf-8

p = {'name':{'first_name':'Tom', 'last_name':'Steven'},
        'job':['dev', 'mgr'],
        'age':18
        }

print(p['name'])
print(p['name']['first_name'])
print(p['job'])

#for key, value in p.items():
#    print('key is:{}, value is:{}'.format(key, value))
#
#def MyStuff(object):
#
#    def __init__(self, targerine):
#        self.targerine = targerine
#
#    def apple(self):
#        print('I AM CLASSY APPLES!')
#
#thing = MyStuff()
#thing.apple()
#print(thing.targerine)

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday_song = [
        'Happy birthday to you',
        'I don\'t want to get sued',
        'So I\'ll stop right there'
        ]

happy_bday = Song(happy_bday_song)
happy_bday.sing_me_a_song()
