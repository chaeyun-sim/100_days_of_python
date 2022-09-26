import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = '21318067ee3e4dd09172560f6b55514f'
CLIENT_SECRET = '8af83d37559e423e9abfad7b72170601'
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date = '2000-08-12'
splited = date.split('-')

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')

info = soup.find_all(name='h3', class_="a-no-trucate")
titles = [items.getText().strip() for items in info]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id = CLIENT_ID,
        client_secret= CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

song_uri = []
user_id = sp.current_user()['id']
year = splited[0]
for song in titles:
    result = sp.search(
        q=f"track:{song} year:{year}",
        type="track"
    )
    # pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify.")

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False
)

sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uri
)

print("Ok, Done!")