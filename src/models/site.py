#! /usr/bin/python
# Copyright (C) 2020 thanhvu9406@gmail.com

from .base import BaseModel


class BaseSiteModel(BaseModel):
    """
        Base Site Model
    """

    _url = ''       # Site URL
    columns = {     # Column of collections to crawl

    }

    @classmethod
    def get_site_url(cls):
        return cls._url

class Gmarket(BaseSiteModel):
    """
        Site to crawler object
    """
    _url = 'http://gpromotion.gmarket.co.kr/'
    _sale_url = ''