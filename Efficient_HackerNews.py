# Scrapping the site for an efficient daily intake of news.
import requests
from bs4 import BeautifulSoup
import lxml
import pprint

res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(res.text, "lxml")
soup2 = BeautifulSoup(res2.text, "lxml")

links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

couple_link = links + links2
couple_subtext = subtext + subtext2


def create_custom_hn(links, subtext):
    hacker_news = []

    for index, item in enumerate(links):
        news = links[index].getText()
        news_link = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hacker_news.append({"title": news, "link": news_link, 'votes': points})
    return sorted(hacker_news, key=lambda x: x["votes"], reverse=True)


pprint.pprint(create_custom_hn(couple_link, couple_subtext))
