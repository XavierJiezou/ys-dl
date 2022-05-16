<p align="center">
    <img alt="logo" src="./image/favicon.ico" />
    <h1 align="center">原神下载器</h1>
    <p align="center">一个从<a href="https://bbs.mihoyo.com/ys/">原神社区</a>自动抓取图片的命令行工具。
    </p>
</p>
<p align="center">
    <img src="https://img.shields.io/github/workflow/status/XavierJiezou/ys-dl/Release" alt="GitHub Workflow Status">
    <a
        href="https://www.codacy.com/gh/XavierJiezou/ys-dl/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=XavierJiezou/ys-dl&amp;utm_campaign=Badge_Grade">
        <img src="https://app.codacy.com/project/badge/Grade/c2f85c8d6b8a4892b40059703f087eab" alt="Codacy Badge">
    </a>
    <a href="https://codecov.io/gh/XavierJiezou/ys-dl">
        <img src="https://codecov.io/gh/XavierJiezou/ys-dl/branch/main/graph/badge.svg?token=QpCLcUGoYx" alt="codecov">
    </a>
    <img src="https://img.shields.io/pypi/pyversions/ys-dl" alt="PyPI - Python Version">
    <img src="https://img.shields.io/pypi/dm/ys-dl" alt="PyPI - Downloads">
    <img src="https://img.shields.io/pypi/v/ys-dl" alt="PyPI">
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
    <a href="#演示">观看演示</a>
    •
    <a href="https://github.com/xavierjiezou/ys-dl/issues/new">报告错误</a>
    •
    <a href="https://github.com/xavierjiezou/ys-dl/issues/new">报告功能</a>
  </p>
  <p align="center">
    <a href="/docs/README.en.md">English </a>
    •
    <a href="/docs/README.cn.md">简体中文</a>
  </p>
</p>
<p align="center">喜欢这个项目吗？请考虑捐赠<a href="https://paypal.me/xavierjiezou?country.x=C2&locale.x=zh_XC">（<a href="https://cdn.jsdelivr.net/gh/XavierJiezou/ys-dl@main/image/wechat.jpg">微信</a> | <a href="https://cdn.jsdelivr.net/gh/XavierJiezou/ys-dl@main/image/alipay.jpg">支付宝</a>）</a>，以帮助它改善！

## 演示

![demo](./image/demo.png)

## 功能

- [x] 原神[官网](https://ys.mihoyo.com/)图标下载
- [x] 原神[官网](https://ys.mihoyo.com/)背景图片下载
- [x] 原神社区 [COS](https://bbs.mihoyo.com/ys/home/49) 图下载
- [x] 原神社区[同人图](https://bbs.mihoyo.com/ys/home/29)下载
- [x] 原神社区 [COS 榜](https://bbs.mihoyo.com/ys/imgRanking/49/1)与[同人榜](https://bbs.mihoyo.com/ys/imgRanking/29/1)下图片载
- [ ] 原神社区[话题标签](https://bbs.mihoyo.com/ys/topicDetail/558)所属图片下载

## 安装

```bash
pip install ys-dl
```

---

`ys-dl`是基于 [selenium](https://www.selenium.dev/) 开发的。目前唯一支持的浏览器是 Chrome，因此你的系统必须安装有 Chrome 浏览器，并下载 [Chrome WebDriver](https://chromedriver.chromium.org/downloads) 放入 Python 安装目录。（想了解关于 WebDriver 的详细信息？请参阅[这里](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)。）

## 用法

`$ ys-dl`

- 原神社区 [COS](https://bbs.mihoyo.com/ys/home/49) 图片下载

```bash
ys-dl cos
```

- 原神社区[同人图](https://bbs.mihoyo.com/ys/home/29)下载

```bash
ys-dl fan
```

- 根据排名（日榜 | 周榜 | 月榜）下载原神社区 [COS 图](https://bbs.mihoyo.com/ys/imgRanking/49/1)或[同人图](https://bbs.mihoyo.com/ys/imgRanking/29/1)

```bash
ys-dl rank
```

## 更新

更新日志见 [CHANGELOG.md](CHANGELOG.md)

## 证书

[MIT License](License)

## 参考

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=python-poetry&repo=poetry)](https://github.com/python-poetry/poetry)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=SeleniumHQ&repo=selenium)](https://github.com/SeleniumHQ/selenium)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=psf&repo=requests)](https://github.com/psf/requests)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=Textualize&repo=rich)](https://github.com/Textualize/rich)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=google&repo=python-fire)](https://github.com/google/python-fire)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=pytest-dev&repo=pytest)](https://github.com/pytest-dev/pytest)
