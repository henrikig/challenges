from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re
from copy import copy

import requests
from bs4 import BeautifulSoup
from nltk.corpus import wordnet as wn

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
REPLACE_CHARS = str.maketrans("-", " ")


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open(RSS_FEED, 'r') as rss:
        tag_string = "".join(rss.readlines())
        all_tags = TAG_HTML.findall(tag_string)
        return [tag.translate(REPLACE_CHARS) for tag in all_tags]


def get_tags_from_live_site():
    page = requests.get("http://pybit.es/feeds/all.rss.xml")
    soup = BeautifulSoup(page.text, "lxml")
    categories = [c.get_text().lower().strip() for c in soup.find_all("category")]
    return categories


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    tags = copy(tags)
    top_tags = Counter(tags).most_common(TOP_NUMBER)
    return top_tags


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    for pair in product(tags, tags):
        # Check if first characters are not matching for performance enchantments
        if pair[0][0] != pair[1][0]:
            continue
        pair = tuple(sorted(pair))
        similarity = SequenceMatcher(None, *pair).ratio()
        if SIMILAR < similarity < IDENTICAL:
            yield pair


if __name__ == "__main__":
    main_tags = get_tags()
    main_top_tags = get_top_tags(main_tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in main_top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(set(main_tags)))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
