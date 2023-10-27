import bs4
import requests
import re


with open('Automate_the_boring_stuff/web_scraping_with_bs4/test.html') as my_url:
    page_soup = bs4.BeautifulSoup(my_url, 'lxml')

containers = page_soup.find("div", {"class":"position-rel"})
contain = containers.div.p.text
print(contain)

contain1 = containers.div['class']
print(contain1)


