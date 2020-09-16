import requests
from bs4 import BeautifulSoup
import pprint

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def createCustomHN(links, subtext):
    listHN = []

    for idx, item in enumerate(links):

        
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                listHN.append({'title': title, 'link': href, 'votes': points})
      
    return sort_stories_by_votes(listHN)


if __name__ == '__main__':
    res = requests.get('https://news.ycombinator.com/news?p=1')
    soup = BeautifulSoup(res.text, 'html.parser')
    megaLinks = soup.select('.storylink')
    megaSubTexts = soup.select('.subtext')

    for pgNumber in range(2,10):
        res = requests.get('https://news.ycombinator.com/news?p='+str(pgNumber))
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.storylink')
        subtext = soup.select('.subtext')
        megaLinks = megaLinks + links
        megaSubTexts = megaSubTexts + subtext

    pprint.pprint(createCustomHN(megaLinks, megaSubTexts))