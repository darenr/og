#!/usr/bin/env python
# -*- coding: utf-8 -*--

import requests
import sys
import json
import re
from bs4 import BeautifulSoup


def grab_meta_tags(soup, patterns):
    result = {}
    for k, v in patterns:
        for meta in soup.findAll(attrs={k: re.compile(v)}):
            if meta and meta.has_attr('content'):
                result[meta[k].replace(':', '_')] = meta['content']
    return result


def get_og_tags(url, headers):
    page = requests.get(url, headers=headers)
    return grab_meta_tags(BeautifulSoup(page.text, 'lxml'), [
        ('property', 'og:*'),
        ('name', 'og:*'),
        ('name', 'sailthru[.]*'),
        ('name', 'twitter:*')])


if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Referer': 'https://googlebot.com',
        'Accept-Charset': 'utf-8',
        "Accept-Encoding": "identity, deflate, compress, gzip",
        'Connection': 'close'
    }
    for url in sys.argv[1:]:
        print json.dumps(get_og_tags(url, headers), indent=2)
