#!/usr/bin/env python
# encoding: utf-8

# install pyenv
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

# 镜像
v=3.5.2|wget http://mirrors.sohu.com/python/$v/Python-$v.tar.xz -P ~/.pyenv/cache/;pyenv install $v

# 刷新
pyenv rehash

# 切换shell
pyenv shell 3.5.3
