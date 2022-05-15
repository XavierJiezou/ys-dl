import os
import random
import time

from selenium import webdriver
import toml

from ys_dl.core import YsDl
from ys_dl.apis import APIS


class TestYsDl(YsDl):

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    def test_version(self):
        project = toml.load('pyproject.toml')
        version = project['tool']['poetry']['version']
        assert self.version == version

    def test_dl_img_static(self):
        sample = {
            'https://upload-bbs.mihoyo.com/upload/2022/05/01/301685713/8f168d7cd4aef6c7f556d882712fc379_1319607209990236918.jpg': 3234434,
            'https://upload-bbs.mihoyo.com/upload/2022/05/04/295576484/2f9846ab3f86700ec6d9ebf1da034f48_2276417862705020206.jpg': 7658847,
            'https://upload-bbs.mihoyo.com/upload/2022/05/09/214325571/ce6a12088bbbfa629b4d5fc46f31f271_2525566984544398307.jpg': 4003035,
        }
        for url in sample:
            name = os.path.basename(url)
            self.dl_img_static(url, name)
            size = os.path.getsize(name)
            assert size == sample[url]
            time.sleep(1)

    def test_dl_img_dynamic(self):
        sample = {
            'https://upload-bbs.mihoyo.com/upload/2022/05/01/301685713/8f168d7cd4aef6c7f556d882712fc379_1319607209990236918.jpg': 3234434,
            'https://upload-bbs.mihoyo.com/upload/2022/05/04/295576484/2f9846ab3f86700ec6d9ebf1da034f48_2276417862705020206.jpg': 7658847,
            'https://upload-bbs.mihoyo.com/upload/2022/05/09/214325571/ce6a12088bbbfa629b4d5fc46f31f271_2525566984544398307.jpg': 4003035,
        }
        driver = webdriver.Chrome(options=self.options)
        for url in sample:
            save_dir = os.getcwd()
            img_name = os.path.basename(url)
            save_path = os.path.join(save_dir, img_name)
            if os.path.exists(save_path):
                pass
            else:
                self.dl_img_dynamic(url, save_path, driver)
                size = os.path.getsize(save_path)
                assert size == sample[url]
        driver.quit()

    def test_dl_img(self):
        sample = {
            'https://upload-bbs.mihoyo.com/upload/2022/05/01/301685713/8f168d7cd4aef6c7f556d882712fc379_1319607209990236918.jpg': 3234434,
            'https://upload-bbs.mihoyo.com/upload/2022/05/04/295576484/2f9846ab3f86700ec6d9ebf1da034f48_2276417862705020206.jpg': 7658847,
            'https://upload-bbs.mihoyo.com/upload/2022/05/09/214325571/ce6a12088bbbfa629b4d5fc46f31f271_2525566984544398307.jpg': 4003035,
        }
        driver = webdriver.Chrome(options=self.options)
        for url in sample:
            save_dir = os.getcwd()
            img_name = os.path.basename(url)
            save_path = os.path.join(save_dir, img_name)
            if os.path.exists(save_path):
                pass
            else:
                mode = random.choice(['static', 'dynamic'])
                self.dl_img(url, mode, save_dir, img_name, driver)
                size = os.path.getsize(save_path)
                assert size == sample[url]
        driver.quit()

    def test_get_icon_img(self):
        result = self.get_icon_img()
        icon_url = result['data']
        assert '.ico' in icon_url

    def test_get_bg_img(self):
        result = self.get_bg_img()
        bg_url = result['data']
        assert '.jpg' in bg_url

    def test_get_article_url(self):
        sample = {
            'cos-rank-daily': 1,
            'cos-rank-daily': 20,
            'cos-rank-daily': 100,
            'cos-hot': 1,
            'cos-hot': 20,
            'cos-hot': 100,
            'cos-latest_post': 1,
            'cos-latest_post': 20,
            'cos-latest_post': 100,
            'cos-latest_reply': 1,
            'cos-latest_reply': 20,
            'cos-latest_reply': 100,
            'fan-rank-daily': 1,
            'fan-rank-daily': 100,
            'fan-rank-daily': 200,
            'fan-hot': 1,
            'fan-hot': 20,
            'fan-hot': 100,
            'fan-latest_post': 1,
            'fan-latest_post': 20,
            'fan-latest_post': 100,
            'fan-latest_reply': 1,
            'fan-latest_reply': 20,
            'fan-latest_reply': 100,
        }
        self.options.add_argument('--headless')
        driver = webdriver.Chrome(options=self.options)
        for key in sample:
            result = self.get_article_url(
                driver,
                *key.split('-'),
                sample[key]
            )
            if 'rank' not in key:
                tmp_var = sample[key]
            else:
                if 'cos' in key:
                    limit_length = 20
                else:
                    limit_length = 100
                tmp_var = min(sample[key], limit_length)
            assert tmp_var == len(result['data'])
        driver.quit()

    def test_get_article_img(self):
        sample = {
            'https://bbs.mihoyo.com/ys/article/21477272': 9,
            'https://bbs.mihoyo.com/ys/article/21735163': 4,
            'https://bbs.mihoyo.com/ys/article/22054203': 3,
            'https://bbs.mihoyo.com/ys/article/21398220': 1,
            'https://bbs.mihoyo.com/ys/article/22255184': 5,
            'https://bbs.mihoyo.com/ys/article/22142359': 2,
        }
        self.options.add_argument('--headless')
        driver = webdriver.Chrome(options=self.options)
        for url in sample:
            result = self.get_article_img(url, driver)
            assert len(result['data']['urls']) == sample[url]
        driver.quit()
