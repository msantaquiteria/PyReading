'''
Created on 6/5/2016
    Scrap module. It only works on wuxiaworld.com for now
@author: msant
'''

import requests
import lxml
import sys
from bs4 import BeautifulSoup

def webScrap(url, file):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    
    #Text parsed by bs4
    raw = soup.get_text()
    content = raw.split('Previous Chapter Next Chapter ')[1]

    f = open(file, 'w')
    f.write(content.encode('utf-8'))
    f.close()

webScrap('http://www.wuxiaworld.com/tdg-index/tdg-chapter-221/','Lecture.txt')

