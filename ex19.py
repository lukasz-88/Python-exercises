"""
Exercise 19: Decode A Web Page Two
Using the requests and BeautifulSoup Python libraries,
print to the screen the full text of the article on this website:
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
(article is no longer on 4 pages!)

The article is long, so it is split up between 4 pages.
Your task is to print out the text to the screen so that you can
read the full article without having to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup and
requests libraries through the solution of the exercise posted here.)

This will just print the full text of the article to the screen.
It will not make it easy to read, so next exercise we will learn how to
write this text to a .txt file.
"""

import requests
from bs4 import BeautifulSoup

for page_number in range(1, 3):
    # new_ulr with article on 2 pages
    url = "http://content.time.com/time/magazine/article/0,9171,2005869-" + \
        str(page_number) + ",00.html"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    articles = soup.find_all("p")

    for article in articles:
        print(article.text)
