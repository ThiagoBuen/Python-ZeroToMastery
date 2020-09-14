#beautifulsoup4
#requests

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.body)
#print(soup.find_all('div'))
#print(soup.find_all('a'))
#print(soup.a)
#print(soup.find('a'))
#print(soup.find(id='24472941'))
#print(soup.select('#score_24468874'))
links = soup.select('.storylink')
votes = soup.select('.score')
#print(votes[0])
#print(votes[0].get('id'))
