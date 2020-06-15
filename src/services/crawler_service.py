#! /usr/bin/python
# Copyright (C) 2020 thanhvu9406@gmail.com

from ..models import Gmarket
from .base import BaseService
from .browser_service import Chrome


class CrawlerService(BaseService):
    _site = None

    @classmethod
    def connect_to_site(cls):
        site_url = cls._site.get_site_url()
        conn = Chrome().get_conn()
        return conn.get(site_url)


class GmarketCrawlerService(CrawlerService):
    _site = Gmarket
