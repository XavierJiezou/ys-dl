import os
import random
import time

from selenium import webdriver
import toml

from ys_dl.cli import YsDlCli
from ys_dl.apis import APIS


class TestYsDlCli(object):

    ysdlcli = YsDlCli()

    def test_init(self):
        try:
            self.ysdlcli
        except:
            raise

    def test_version(self):
        project = toml.load('pyproject.toml')
        version = project['tool']['poetry']['version']
        assert self.ysdlcli.version == version

    def test_icon(self):
        pass

    def test_bg(self):
        pass

    def test_get_article_label(self):
        pass

    def test_get_rank_key(self):
        pass

    def test_get_dl_limit(self):
        pass

    def test_dl_img_loop(self):
        pass

    def test_cos(self):
        pass

    def test_fan(self):
        pass

    def test_rank(self):
        pass

    def test_topic(self):
        pass
