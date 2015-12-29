# !/usr/bin/env python2
#  -*- coding: UTF-8 -*-
#  File: __init__.py
#  Author: Yuxin Wu <ppwwyyxx@gmail.com>

from pkgutil import walk_packages
import os
import os.path

def global_import(name):
    print name
    p = __import__(name, globals(), locals())
    lst = p.__all__ if '__all__' in dir(p) else dir(p)
    for k in lst:
        globals()[k] = p.__dict__[k]

for _, module_name, _ in walk_packages(
        [os.path.dirname(__file__)]):
    if not module_name.startswith('_'):
        global_import(module_name)

