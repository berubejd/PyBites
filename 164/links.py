#!/usr/bin/env python3.8

import sys

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


def make_html_links():
    for line in sys.stdin:
        if not line.startswith("http"):
            continue

        line = line.split(",")
        if len(line) > 2:
            continue

        url = line[0].strip()
        text = line[1].strip()

        target = ' target=\"_blank\"' if not 'pybit.es' in url.lower() and not 'codechalleng.es' in url.lower() else ''

        print(f'<a href="{url}"{target}>{text}</a>')


if __name__ == '__main__':
    make_html_links()


'''
Bite 164. CLI tool: HTML link converter (stdin to stdout) ☆
In this Bite you are going to help your team out automating a boring task.

They reached out to you with some data files that contain lines of (link_href, link_name). Unfortunately they also contain bad data.

The additional requirement is that your script can receive piped output from another process (read on ...)

Code up make_html_links that reads in data from stdin (use sys) and converts it to proper HTML:

Ignore the bad lines (no http in line, more than one comma, etc),
Strip white spaces around link_href and link_name,
Final twist: if the domain is NOT pybit.es or codechalleng.es make it an external link by adding target="_blank" to the resulting HTML.
Make the function print to standard output, don't return anything. The tests run your code as below and hence check standard output!
Running your program, which is automatically saved in a module called links.py, it should work like this:

$ cat data1
https://www.python.org, Python Homepage
bad data,blabla,123
https://pybit.es/generators.html , Generators are Awesome
more bad data

$ cat data1|python links.py
<a href="https://www.python.org" target="_blank">Python Homepage</a>
<a href="https://pybit.es/generators.html">Generators are Awesome</a>

$ cat data2
bogus data, again
https://codechalleng.es/bites/ , Bites of Py
https://stackoverflow.com/a/12927564,How to capture subprocess.call stdout
https://pybit.es/,Our labor of love
https://pybit.es/pages/about.html, About Us
https://nu.nl, Dutch news site

$ cat data2|python links.py
<a href="https://codechalleng.es/bites/">Bites of Py</a>
<a href="https://stackoverflow.com/a/12927564" target="_blank">How to capture subprocess.call stdout</a>
<a href="https://pybit.es/">Our labor of love</a>
<a href="https://pybit.es/pages/about.html">About Us</a>
<a href="https://nu.nl" target="_blank">Dutch news site</a>
Pretty cool/useful, no? Make your team happy and increase your coding ninja reputation in your org ;) - have fun and keep calm and code in Python!
'''