import bs4
import requests


def getLaptopPrice(productUrl, selector, ids):
    res = requests.get(productUrl)

    if not res.raise_for_status():
        soup = bs4.BeautifulSoup(res.content, 'html.parser')
        title = soup.select(selector)[0].get_text().strip()
        price = soup.find(id=ids).text.strip()
        return title, price


title, price = getLaptopPrice('https://www.sastodeal.com/ilife-zed-pc-intel-celeron-apollo-lake-n3350-17-3-inch-touch-32gb-hard-drive-3gb-ram-white-lif-sa-a.html'
                       ,'#maincontent > div.columns > div > div.product-info.pdpWrapper > div.row > div.product-info-main.col-md-7 > div.page-title-wrapper.product > h1 > span'
                       , 'product-price-68743')
print(f'\n{title}\n\nThe laptop price is : {price}\n')

