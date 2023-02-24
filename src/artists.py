from requests import get
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

class Artists:

    def __init__(self):
        pass

    def get_artists(self, playlist):
        match playlist:
            case "samba_pe_no_chao":
                ids = []
                
                with open("src/"+playlist+".txt") as f:
                    artists = [line.rstrip() for line in f]

                for artist in artists:
                    ids.append(self.get_artist_id(artist))

                return ids
                    
            case "roda_de_sampa":
                ids = []

                with open("src/"+playlist+".txt") as f:
                    artists = [line.rstrip() for line in f]

                for artist in artists:
                    ids.append(self.get_artist_id(artist))

                return ids

    def get_artist_id(self, artist):
        result = spotify.search(q='artist:' + artist, type='artist', limit=1)
        id = result["artists"]["items"][0]["uri"]
        return id