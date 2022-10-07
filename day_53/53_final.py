from bs4 import BeautifulSoup
import requests
import json

FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSewrRxTxQmPx5TXXp3IlKJoVCUEhuSopqYGhMEX35yly_Q45Q/viewform?usp=sf_link'

header = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)Version/15.6.1 Safari/605.1.15",
    "Accept-Language": "ko-KR,ko;q=0.9"
}
zillow = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
response = requests.get(url=zillow, headers=header)
soup = BeautifulSoup(response.text, 'lxml')

print("\n ----------------------------- \n")

divs = soup.findAll('script', type='application/json')
lst = [items.text for items in divs]
print(lst)

di = json.loads(str(lst[1].strip("<!--""-->")))
print(di)  # cat1까지 찾아봄 ㅠㅠ
whole_list = lst[1].split(",")

print("\n ----------------------------- \n")
prices = []
urls = []
for items in whole_list:
    if "detailUrl" in items:
        url_to_use = items.split('"')[3]
        if "zillow" not in url_to_use:
            url = f"https://www.zillow.com{url_to_use}"
        else:
            url = url_to_use
        urls.append(url)
# print(prices)
# for items in units_list:
#     print(items)
#     if "units" in items:
#         print(items)
# print(urls)
