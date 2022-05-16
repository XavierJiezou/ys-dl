import os
import re
import time
from typing import Any

from fake_useragent import UserAgent
import pyautogui
import pyperclip
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from ys_dl.apis import APIS
from ys_dl import __version__


class YsDl(object):

    @property
    def version(self):
        return __version__

    def dl_img_static(
        self,
        img_url: str,
        save_path: str,
    ) -> dict[str, Any]:
        headers = {'user-agent': UserAgent().random}
        res = requests.get(img_url, headers=headers)
        if res.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(res.content)
            return {
                'status': res.status_code,
                'data': save_path,
                'msg': 'success',
            }
        else:
            return {
                'status': res.status_code,
                'data': None,
                'msg': 'failure',
            }

    def dl_img_dynamic(
        self,
        img_url: str,
        save_path: str,
        driver: webdriver,
    ) -> dict[str, Any]:
        driver.get(img_url)
        driver.implicitly_wait(5)
        pyautogui.hotkey('ctrlleft', 's')
        time.sleep(1)
        pyperclip.copy(save_path)
        time.sleep(0.5)
        pyautogui.hotkey('ctrlleft', 'v')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(1)
        if os.path.exists(save_path):
            return {
                'status': 200,
                'data': save_path,
                'msg': 'success',
            }
        else:
            return {
                'status': 404,
                'data': None,
                'msg': 'failure',
            }

    def dl_img(
        self,
        img_url: str,
        mode: str = 'static',
        save_dir: str = None,
        img_name: str = None,
        driver: webdriver = None,
    ) -> dict[str, Any]:
        if not save_dir:
            save_dir = os.getcwd()
        else:
            os.makedirs(save_dir, exist_ok=True)
        if not img_name:
            img_name = os.path.basename(img_url)
        else:
            pass
        save_path = os.path.join(save_dir, img_name)
        if os.path.exists(save_path):
            return {
                'status': 200,
                'data': save_path,
                'msg': 'success',
            }
        else:
            if mode == 'static':
                return self.dl_img_static(img_url, save_path)
            else:
                return self.dl_img_dynamic(img_url, save_path, driver)

    def get_icon_img(
        self,
        api_key: str = 'icon',
        size: int = 256,
    ) -> dict[str, Any]:
        url = APIS.get(api_key).get(size)
        return {
            'status': 200,
            'data': url,
            'msg': 'success'
        }

    def get_bg_img(self, api_key: str = 'bg') -> dict[str, Any]:
        url = APIS.get(api_key)
        headers = {'user-agent': UserAgent().random}
        res = requests.get(url=url, headers=headers)
        if res.status_code == 200:
            pattern = re.compile('https://web.*?config_.*?.js')
            js_url = re.findall(pattern, res.text)[0]
            js_res = requests.get(url=js_url, headers=headers)
            if js_res.status_code == 200:
                pattern = re.compile('resources":{"(.*?.jpg)"')
                bg_url = re.findall(pattern, js_res.text)[0]
                return {
                    'status': js_res.status_code,
                    'data': bg_url,
                    'msg': 'success'
                }
            else:
                return {
                    'status': js_res.status_code,
                    'data': None,
                    'msg': 'failure'
                }
        else:
            return {
                'status': res.status_code,
                'data': None,
                'msg': 'failure'
            }

    def get_article_url(
        self,
        driver: webdriver,
        api_key: str = 'cos',
        sub_key: str = 'rank',
        rank_key: str = 'daily',
        url_nums: int = 100,
        max_trying: int = 100,
    ) -> dict[str, Any]:
        url = APIS[api_key][sub_key]
        if sub_key == 'rank':
            url_nums = min(url['limit_length'], url_nums)
            url = url[rank_key]
        else:
            pass
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        count = 0
        for _ in range(max_trying):
            tag_a = driver.find_elements(
                By.CSS_SELECTOR,
                APIS['css_selector']['article']['url'],
            )
            if len(tag_a) >= url_nums:
                break
            else:
                action.send_keys(Keys.PAGE_DOWN).perform()
                time.sleep(0.5)
                count += 1
        if count < max_trying:
            urls = []
            for _ in tag_a[:url_nums]:
                urls.append(_.get_attribute('href'))
            return {
                'status': 200,
                'data': urls,
                'msg': 'success',
            }
        else:
            return {
                'status': 404,
                'data': None,
                'msg': 'failure'
            }

    def get_article_img(
        self,
        article_url: str,
        driver: webdriver,
        size: str = 'large'
    ) -> dict[str, Any]:
        driver.maximize_window()
        driver.get(article_url)
        driver.implicitly_wait(5)
        value = APIS['css_selector']['article']['title']
        title = driver.find_element(By.CSS_SELECTOR, value).text
        value = APIS['css_selector']['article']['image']
        image = driver.find_elements(By.CSS_SELECTOR, value)
        if image:
            if size == 'large':
                urls = [_.get_attribute('large') for _ in image]
            else:
                urls = [_.get_attribute('src') for _ in image]
            return {
                'status': 200,
                'data': {
                    'title': title,
                    'urls': urls,
                },
                'msg': 'success'
            }
        else:
            return {
                'status': 404,
                'data': None,
                'msg': 'failure'
            }
    
    def get_article(self):
        pass

    # TODO (GitHub@XavierJiezou): Download images belonging to topic tags.
    def get_topic_url(self):
        pass

    # TODO (GitHub@XavierJiezou): Download images belonging to topic tags.
    def get_topic_img(self):
        pass

    # TODO (GitHub@XavierJiezou): Download images belonging to topic tags.
    def get_topic(self):
        pass


if __name__ == '__main__':
    pass
