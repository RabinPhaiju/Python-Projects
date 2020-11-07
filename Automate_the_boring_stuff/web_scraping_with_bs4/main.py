import bs4
import requests
import re


my_url = 'https://www.sastodeal.com/work-from-home-essentials/laptops.html'
res = requests.get(my_url)
if res.raise_for_status():
    exit()
else:
    page_soup = bs4.BeautifulSoup(res.content, 'html.parser')

containers = page_soup.findAll("div", {"class":"product-item-info"})
header = "product_name, product_price\n"
with open('products.csv', 'w') as f:
    f.write(header)

    count = 1
    for contain in containers:
        count += 1
        name = contain.div.a.text.strip().replace(',','|')
        link = contain.div.a['href']
        prices = contain.div.findAll("div", {"class":"price-box"})
        price = prices[0].findAll("span",{'class':'price-wrapper'})[0].span.text.replace(",","")
        f.write(name + "," + price[2:] + "," + link +"\n")
        if len(containers) == count:
            break


