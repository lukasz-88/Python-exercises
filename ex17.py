'''
Exercise 17: Decode A Web Page
Use the BeautifulSoup and requests Python packages to print out a list
of all the article titles on the New York Times homepage.
https://www.nytimes.com/
'''

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

html_classes = ['css-1m5bs2v esl82me0',
                'css-1qwxefa esl82me0',
                'css-n2blzn esl82me0']

titles_list = soup.find_all(class_ = html_classes)

for title in titles_list:
    print(title.string)
