import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

articles = soup.find_all(name="h3", class_="title")
titles_lst = [items.getText() for items in articles]
movies = list(reversed(titles_lst))
# other way 1: titles_lst[::-1]
# other way 2:
# for n in range(len(titles_lst) - 1, 0, -1):
#     titles_lst[n]

with open('./movies.txt', 'w') as file:
    for item in movies:
        file.write(f"{item}\n")
print('Done!')
