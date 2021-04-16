This is a program that uses python, Javascript, and Youtube and Spotify API's to automatically generate a Spotify playlist from liked Youtube music videos.

## Technologies:
- Python
- [Youtube Data API](https://developers.google.com/youtube/v3)
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)

## How to Run
- Install dependencies `pip3 install -r requirements.txt`
- Get Spotify ID and OAuth Token from Spotify for secrets.py
- Enable OAuth for Youtube and download client_secrets.json
- Run `python3 create_playlist.py`
- Log in to Google Account and get `authorization code` after running
