'''
Exercise 21: Write To A File
Take the code from the How To Decode A Website exercise (if you didn’t
do it or just want to play with some different code, use the code from the
solution), and instead of printing the results to a screen, write the
results to a txt file. In your code, just make up a name for the file
you are saving to.

Extras:
Ask the user to specify the name of the output file that will be saved.
'''

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

filename = input("Enter the filename: ")

html_classes = ['css-hy3emn esl82me0',
                'css-1m5bs2v esl82me0',
                'css-1qwxefa esl82me0',
                'css-n2blzn esl82me0']

titles_list = soup.find_all(class_=html_classes)

with open(filename + '.txt', 'w') as file:
    for title in titles_list:
        file.write(title.string + '\n')
