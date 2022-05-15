import json
import os
import time

import fire
from rich.console import Console
from rich.progress import Progress
from rich.progress import SpinnerColumn
from rich.progress import MofNCompleteColumn
from rich.progress import TimeElapsedColumn
from rich.prompt import Prompt, IntPrompt
from rich.theme import Theme
from selenium import webdriver

from ys_dl.core import YsDl


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
            prompt='Select the rank',
            choices=['daily', 'weekly', 'monthly'],
            default='daily',
        )

    def _get_dl_limit(self, max_value: int) -> int:
        while True:
            limit = IntPrompt.ask(
                prompt=f'Enter the number of pages to download [b][magenta][0~{max_value}][/magenta][/b]',
                default=20,
            )
            if 0 <= limit <= max_value:
                break
            self.console.print(
                f':pile_of_poo: [prompt.invalid]Number must be between 0 and {max_value}')
        return limit

    def _dl_img_loop(self, article_urls: list[str], driver: webdriver) -> None:
        for idx, url in enumerate(article_urls):
            image = YsDl().get_article_img(url, driver)
            title = image['data']['title']
            links = image['data']['links']
            save_dir = os.path.join(
                os.getcwd(),
                'cos',
                f'[{idx+1}] {title}'
            )
            for _idx, _url in enumerate(links):
                YsDl().dl_img(
                    img_link=_url,
                    save_dir=save_dir,
                    img_name=f'{_idx+1}',
                )
                time.sleep(1)
        with self.progress:
            task1 = self.progress.add_task("[green]Overall", total=1000)
            task2 = self.progress.add_task("[cyan]Jobs", total=1000)
            while not self.progress.finished:
                self.progress.update(task1, advance=1)
                self.progress.update(task2, advance=1)
                self.console.print('Working on job #')

    def cos(self) -> None:
        label = self._get_article_label()
        if label == 'rank':
            rank_key = self._get_rank_key()
            with self.console.status('Creating a webdriver'):
                self.options.add_argument('--headless')
                driver = webdriver.Chrome(options=self.options)
            with self.console.status('Getting urls to articles'):
                result = YsDl().get_article_url(driver, rank_key=rank_key)
            limit = self._get_dl_limit(20)
            self._dl_img_loop(result['data'][:limit], driver)
            driver.quit()
        else:
            return label

    def fan(self):
        pass

    def rank(self):
        pass

    # TODO (GitHub@XavierJiezou): Download images belonging to topic tags.
    def topic(self) -> str:
        return 'TODO (GitHub@XavierJiezou): Download images belonging to topic tags.'


def main():
    fire.Fire(YsDlCli)


if __name__ == '__main__':
    main()
