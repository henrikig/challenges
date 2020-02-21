"""
Turn the following unix pipeline into Python code using generators

$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""

from glob import iglob
import re
from collections import Counter


def gen_files(pat):
    yield from iglob(pat)


def gen_lines(files):
    for filepath in files:
        with open(filepath) as f:
            yield from f.readlines()


def gen_grep(lines, pattern):
    regex = re.compile(pattern)
    for line in lines:
        m = regex.match(line.rstrip())
        if m:
            yield m.group()


def gen_count(modules):
    yield from Counter(modules).most_common()


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    modules = gen_grep(lines, r'^import (\w+)')
    counts = gen_count(modules)
    for k, v in counts:
        print(v, k)
