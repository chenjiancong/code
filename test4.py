#!/usr/bin/env python
# encoding: utf-8


def make_bold(func):
    def warrper(*args, **kw):
        print('<b>{}</b>'.format(func))
        return func(*args, **kw)
    return warrper

@make_bold
def get_content():
    return 'Hello world'
print(get_content())

