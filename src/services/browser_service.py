#! /usr/bin/python
# Copyright (C) 2020 thanhvu9406@gmail.com

import os
from selenium import webdriver

from .base import BaseService
from ..utils import get_driver_path

class BaseBrowserService(BaseService):
    """
        Base Browser Service
    """
    _browser_name = ''
    _conn = None

    @classmethod
    def get_conn(cls):
        return cls._conn


class Chrome(BaseBrowserService):
    _browser_name = 'Chrome'

    def __init__(self):
        # create new connection
        self.__setup_connection()

    @classmethod
    def __setup_connection(cls):
        cls._conn = webdriver.Chrome(os.path.join(get_driver_path(), 'chromedriver'))
