"""A summary of interesting image APIs to https://bbs.mihoyo.com/ys/"""


from ast import Pass


APIS = {
    'icon': {
        32: 'https://ys.mihoyo.com/main/favicon.ico',
        256: 'https://genshin.mihoyo.com/favicon.ico',
    },
    'bg': 'https://ys.mihoyo.com/',
    'cos': {

        'hot': 'https://bbs.mihoyo.com/ys/home/49?type=hot',
        'latest_reply': 'https://bbs.mihoyo.com/ys/home/49?type=1',
        'latest_post': 'https://bbs.mihoyo.com/ys/home/49?type=2',
        'rank': {
            'daily': 'https://bbs.mihoyo.com/ys/imgRanking/49/1',
            'weekly': 'https://bbs.mihoyo.com/ys/imgRanking/49/2',
            'monthly': 'https://bbs.mihoyo.com/ys/imgRanking/49/3',
            'limit_length': 20
        },
    },
    'fan': {
        'hot': 'https://bbs.mihoyo.com/ys/home/29?type=hot',
        'latest_reply': 'https://bbs.mihoyo.com/ys/home/29?type=1',
        'latest_post': 'https://bbs.mihoyo.com/ys/home/29?type=2',
        'rank': {
            'daily': 'https://bbs.mihoyo.com/ys/imgRanking/29/1',
            'weekly': 'https://bbs.mihoyo.com/ys/imgRanking/29/2',
            'monthly': 'https://bbs.mihoyo.com/ys/imgRanking/29/3',
            'limit_length': 100
        },
    },
    'topic': { # TODO (GitHub@XavierJiezou): Download images belonging to topic tags.
        'emoji': {
            'new': 'https://bbs.mihoyo.com/ys/topicDetail/105',
            'select': 'https://bbs.mihoyo.com/ys/topicDetail/105?type=1',
            'hot': 'https://bbs.mihoyo.com/ys/topicDetail/105?type=2',
        },
        'wallpaper': {
            'new': 'https://bbs.mihoyo.com/ys/topicDetail/558',
            'hot': 'https://bbs.mihoyo.com/ys/topicDetail/558?type=2',
        },
    },
    'css_selector': {
        'article': {
            'url': 'div.mhy-article-list__body>div>a.mhy-router-link',
            'title': 'div.mhy-article-page__title>h1',
            'image': 'div.mhy-img-article img',
        },
        'topicDetail': {
            'url': '',
            'title': '',
            'image': '',
        },
    },
}


if __name__ == '__main__':
    pass
