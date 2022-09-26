from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_num = max(article_upvote)
index = article_upvote.index(largest_num)
famous_text = article_texts[index]
famous_list = article_links[index]
print(famous_text, famous_list, largest_num)
