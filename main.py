from requests import get
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from src.artists import Artists

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
scope = 'playlist-modify-public'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
Artists = Artists()

def get_top_track(artists):
    tracks = []
    for artist in artists:
        result = spotify.artist_top_tracks(artist)
    
        for track in result["tracks"]:
            if track["album"]["album_type"] != "compilation":
                tracks.append(track["uri"])
                break

    return tracks

def add_tracks_to_playlist(playlist, tracks):
    for track in tracks:
        sp.playlist_remove_all_occurrences_of_items(playlist_id=playlist, items=[track])
        sp.playlist_add_items(playlist_id=playlist, items=[track], position=None)
    return None

def main():
    add_tracks_to_playlist("069RBt0vjJHEhvgYWjJwQx", get_top_track(Artists.get_artists("samba_pe_no_chao")))
    add_tracks_to_playlist("6AyRgI5cVOtnErUgINZmVz", get_top_track(Artists.get_artists("roda_de_sampa")))
    return None

main()
