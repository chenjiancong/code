#!/usr/bin/env python
# encoding: utf-8

def break_words(stuff):
    '''This function will break up words for us.'''
    words = stuff.split(' ')
    return words

def sort_words(words):
    '''Souts the words.'''
    return sorted(words)

def print_first_word(words):
    '''Print the first word after popping it off.'''
    word = words.pop(-1)
    print(word)

a = break_words('a b c')
b = sort_words('cba')
c = print_first_word('Jack')
print(a, b, c)
