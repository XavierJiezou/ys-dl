import json
import os
import re
import time
from typing import Any

import fire
from pytest import param
from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    MofNCompleteColumn,
    TimeElapsedColumn,
)
from rich.prompt import Prompt, IntPrompt
from rich.theme import Theme
from selenium import webdriver

from ys_dl.core import YsDl
from ys_dl.apis import APIS


class YsDlCli(object):

    def __init__(self) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option(
            'excludeSwitches',
            ['enable-logging']
        )
        theme = Theme({
            "success": "cyan",
            "failure": "b red",
        })
        self.console = Console(theme=theme)
        self.progress = Progress(
            SpinnerColumn(),
            MofNCompleteColumn(),
            *Progress.get_default_columns(),
            TimeElapsedColumn(),
            console=self.console,
        )

    @property
    def version(self) -> str:
        return YsDl().version

    def icon(self) -> None:
        size = Prompt.ask(
            prompt='Select the size',
            choices=['256', '32'],
            default='256'
        )
        result = YsDl().get_icon_img(size=int(size))
        if result['status'] == 200:
            with self.console.status(f'Downloading {size}x{size} icon to local'):
                YsDl().dl_img(result['data'])
        else:
            pass
        self.console.print_json(json.dumps(result))

    def bg(self) -> None:
        result = YsDl().get_bg_img()
        if result['status'] == 200:
            with self.console.status('Downloading background image to local'):
                YsDl().dl_img(result['data'], img_name='bg.jpg')
        else:
            pass
        self.console.print_json(json.dumps(result))

    def _get_article_label(self) -> str:
        labels = ['rank', 'hot', 'latest_post', 'latest_reply']
        emojis = [
            ':rocket:',
            ':fire:',
            ':envelope_with_arrow:',
            ':loudspeaker:',
        ]
        tmp_str = '/'.join([f'{e} {l}' for e, l in zip(emojis, labels)])
        return Prompt.ask(
            prompt=f'Enter the label [b][magenta][{tmp_str}][/magenta][/b]',
            choices=labels,
            show_choices=False,
            default='rank',
        )

    def _get_rank_key(self) -> str:
        return Prompt.ask(
            prompt='Select the key',
            choices=['daily', 'weekly', 'monthly'],
            default='daily',
        )

    def _get_rank_api(self) -> str:
        return Prompt.ask(
            prompt='Select the api',
            choices=['cos', 'fan'],
            default='cos',
        )

    def _get_dl_limit(self, max_value: int, default_value: int) -> int:
        while True:
            limit = IntPrompt.ask(
                prompt=f'Enter the number of pages to download [b][magenta][0~{max_value}][/magenta][/b]',
                default=default_value,
            )
            if 0 <= limit <= max_value:
                break
            self.console.print(
                f':pile_of_poo: [prompt.invalid]Number must be between 0 and {max_value}')
        return limit

    def _dl_img_loop(
        self,
        article_urls: list[str],
        driver: webdriver,
        is_rank: bool,
        params: list[Any],
    ) -> None:
        if is_rank:
            overall_desc = f'{params[1]}/{params[0]}/{params[2]}'
        else:
            if params[1] == 'rank':
                overall_desc = '/'.join(params[:3])
            else:
                overall_desc = '/'.join(params[:2])
        with self.progress:
            task = self.progress.add_task(
                description=f'[green]{overall_desc}',
                total=len(article_urls),
            )
            count = 0
            for idx, url in enumerate(article_urls):
                image = YsDl().get_article_img(url, driver)
                title = image['data']['title'].replace(' ', '')
                title = re.sub('[/\\:*?"<>|]', '', title)
                urls = image['data']['urls']
                save_dir = os.path.join(
                    f'{overall_desc}/',
                    f'[{idx+1:0>{len(str(len(article_urls)))}}]{title}/',
                )
                # if len(title)<=10:
                #     _title = title
                # else:
                #     _title = f'{title[:7]}...'
                sub_task = self.progress.add_task(
                    description=f'[cyan][{idx+1:0>{len(str(len(article_urls)))}}]{title}',
                    total=len(urls),
                )
                for _idx, _url in enumerate(urls):
                    YsDl().dl_img(
                        img_url=_url,
                        save_dir=save_dir,
                        img_name=f'{_idx+1}.jpg',
                    )
                    save_path = os.path.join(save_dir, f'{_idx+1}.jpg')
                    link_path = os.path.join(os.getcwd(), save_dir, f'{_idx+1}.jpg')
                    self.console.log(f'Downloaded {save_path}', style=f'link {link_path}')
                    self.progress.update(sub_task, advance=1)
                    time.sleep(1)
                    count += 1
                self.progress.update(task, advance=1)
        with self.console.status('Quitting the webdriver'):
            driver.quit()
        self.console.print(f'[green]{count} images downloaded, done!')

    def _get_params(self, api_key: str, is_rank: bool) -> list[Any]:
        if is_rank:
            sub_key = 'rank'
            rank_key = self._get_rank_key()
            max_value = APIS[api_key][sub_key]['limit_length']
            url_nums = self._get_dl_limit(max_value, max_value)
        else:
            label = self._get_article_label()
            if label == 'rank':
                sub_key = 'rank'
                rank_key = self._get_rank_key()
                max_value = APIS[api_key][sub_key]['limit_length']
                url_nums = self._get_dl_limit(max_value, max_value)
            else:
                sub_key = label
                rank_key = None
                max_value = 500
                url_nums = self._get_dl_limit(max_value, 100)
        return [
            api_key,
            sub_key,
            rank_key,
            url_nums,
        ]

    def _article(self, api_key: str = 'cos', is_rank: bool = False) -> None:
        with self.console.status('Yuanshen downloader booting up'):
            time.sleep(1)
        with self.console.status('Creating a webdriver (headless)'):
            self.options.add_argument('--headless')
            driver = webdriver.Chrome(options=self.options)
        params = self._get_params(api_key, is_rank)
        with self.console.status('Getting urls to articles'):
            result = YsDl().get_article_url(
                driver,
                *params,
            )
        self._dl_img_loop(result['data'], driver, is_rank, params)

    def cos(self) -> None:
        self._article('cos')

    def fan(self) -> None:
        self._article('fan')

    def rank(self) -> None:
        api_key = self._get_rank_api()
        self._article(api_key, is_rank=True)

    # TODO (GitHub@XavierJiezou): Download images belonging to topic tags.
    def topic(self) -> str:
        return 'TODO (GitHub@XavierJiezou): Download images belonging to topic tags.'


def main():
    fire.Fire(YsDlCli)


if __name__ == '__main__':
    main()
