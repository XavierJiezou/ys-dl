<p align="center">
    <img alt="logo" src="https://cdn.jsdelivr.net/gh/XavierJiezou/ys-dl@main/image/favicon.ico" />
<h1 align="center">Yuanshen-Downloader</h1>
<p align="center">Command-line program to download images from <a href="https://bbs.mihoyo.com/ys/">Genshin Impact
        Community</a>.
</p>
</p>
<p align="center">
    <a href="https://github.com/XavierJiezou/ys-dl/actions?query=workflow:Release">
        <img src="https://github.com/XavierJiezou/ys-dl/workflows/Release/badge.svg"
            alt="GitHub Workflow Release Status" />
    </a>
    <a href='https://ys-dl.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/ys-dl/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a
        href="https://www.codacy.com/gh/XavierJiezou/ys-dl/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=XavierJiezou/ys-dl&amp;utm_campaign=Badge_Grade">
        <img src="https://app.codacy.com/project/badge/Grade/c2f85c8d6b8a4892b40059703f087eab" alt="Codacy Badge">
    </a>
    <a href="https://codecov.io/gh/XavierJiezou/ys-dl">
        <img src="https://codecov.io/gh/XavierJiezou/ys-dl/branch/main/graph/badge.svg?token=QpCLcUGoYx" alt="codecov">
    </a>
    <a href="https://pypi.org/project/ys-dl/">
        <img src="https://img.shields.io/pypi/pyversions/ys-dl" alt="PyPI - Python Version">
    </a>
    <a href="https://pypistats.org/packages/ys-dl">
        <img src="https://img.shields.io/pypi/dm/ys-dl" alt="PyPI - Downloads">
    </a>
    <a href="https://pypi.org/project/ys-dl/">
        <img src="https://img.shields.io/pypi/v/ys-dl" alt="PyPI">
    </a>
    <a href="https://github.com/XavierJiezou/ys-dl/stargazers">
        <img src="https://img.shields.io/github/stars/XavierJiezou/ys-dl" alt="GitHub stars">
    </a>
    <a href="https://github.com/XavierJiezou/ys-dl/network">
        <img src="https://img.shields.io/github/forks/XavierJiezou/ys-dl" alt="GitHub forks">
    </a>
    <a href="https://github.com/XavierJiezou/ys-dl/issues">
        <img src="https://img.shields.io/github/issues/XavierJiezou/ys-dl" alt="GitHub issues">
    </a>
    <a href="https://github.com/XavierJiezou/ys-dl/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/XavierJiezou/ys-dl" alt="GitHub license">
    </a>
    <br />
    <br />
    <a href="https://www.python.org/">
        <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt="forthebadge made-with-python">
    </a>
    <a href="https://github.com/XavierJiezou">
        <img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="ForTheBadge built-with-love">
    </a>
</p>
<p align="center">
    <a href="#demo">View Demo</a>
    •
    <a href="https://github.com/xavierjiezou/ys-dl/issues/new">Report Bug</a>
    •
    <a href="https://github.com/xavierjiezou/ys-dl/issues/new">Request Feature</a>
</p>
<p align="center">
    <a href="/docs/README.en.md">English </a>
    •
    <a href="/docs/README.cn.md">简体中文</a>
</p>
<p align="center">Love the project? Please consider <a
        href="https://paypal.me/xavierjiezou?country.x=C2&locale.x=zh_XC">donating</a> to help it improve!</p>

## Demo

![demo](https://cdn.jsdelivr.net/gh/XavierJiezou/ys-dl@main/image/demo.png)

![show](https://cdn.jsdelivr.net/gh/XavierJiezou/ys-dl@main/image/show.png)

## Features

- [x] Download icon image.
- [x] Download background image.
- [x] Download cosplay image.
- [x] Download fan works image.
- [x] Download ranking images.
- [ ] Downlaod topic images.

## Install

```bash
pip install ys-dl
```

---

`ys-dl` is developed based on selenium. Currently, the only supported browser is chrome, you need to download [Chrome WebDriver](https://chromedriver.chromium.org/downloads) and put it in the Python installation directory. For more details about WebDriver, refer to [here](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/).

## Usage

`$ ys-dl`

- Download cosplay images.

```bash
ys-dl cos
```

- Download fan works images.

```bash
ys-dl fan
```

- Download ranking images.

```bash
ys-dl rank
```

## Changelog

See [CHANGELOG.md](/CHANGELOG.md)

## License

[MIT License](/License)

## References

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=python-poetry&repo=poetry)](https://github.com/python-poetry/poetry)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=SeleniumHQ&repo=selenium)](https://github.com/SeleniumHQ/selenium)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=psf&repo=requests)](https://github.com/psf/requests)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=Textualize&repo=rich)](https://github.com/Textualize/rich)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=google&repo=python-fire)](https://github.com/google/python-fire)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=pytest-dev&repo=pytest)](https://github.com/pytest-dev/pytest)
