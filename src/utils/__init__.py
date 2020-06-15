#! /usr/bin/python
# Copyright (C) 2020 thanhvu9406@gmail.com

import os

def get_project_path():
    return os.path.abspath(os.curdir)

def get_driver_path():
    return os.path.join(get_project_path(), 'src/browser_driver')