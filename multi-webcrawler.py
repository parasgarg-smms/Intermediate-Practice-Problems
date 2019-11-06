import random
import string
from multiprocessing import Pool

import bs4 as bs
import requests


def get_random_link():
    random_string = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for i in range(3))
    url = ''.join(['http://', random_string, '.com'])
    return url


def handle_custom_links(url, link):
    if link.startswith('/'):
        return ''.join(url, link)
    elif link.startswith('#'):
        pass
    else:
        return link


def sub_links(url):
    try:
        resp = requests.get(url)
        source = bs.BeautifulSoup(resp.text, 'lxml')
        body = (source.body)
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_custom_links(url, link) for link in links]
        links = [str(link.encode('ascii')) for link in links]
        return links
    except Exception as e:
        print(str(e) + url)
        return []

def main():
    how_many = 4
    p = Pool(processes=how_many)
    total_main_links = [get_random_link() for _ in range(how_many)]
    data = p.map(sub_links, [url for url in total_main_links])
    data = [url for links in data for url in links]
    p.close()

    with open('links.txt', 'w') as f:
        f.write(str(data))


if __name__ == '__main__':
    main()
