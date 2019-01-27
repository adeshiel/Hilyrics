import spotipy
import spotipy.util as util
import musixmatch as mm
from spotipy import oauth2
from flask import Flask, render_template, request
from key import C_ID, SECRET, MMKEY
import requests as req
import json


mm_url = 'http://api.musixmatch.com/ws/1.1/'

scoped = 'playlist-read-private playlist-read-collaborative'

redirect = "http://localhost/"
# redirect = "http://google.com/"
play_names = []
name_to_id = {}
tracks = []
arttitle = []

genres = {}



# get from front

def getUsername():
    return "me"

username = "ashley.deshields.2016@gmail.com"

def runall():
    authorize()
    token = util.prompt_for_user_token(username, 'playlist-read-private playlist-read-collaborative', client_id=C_ID, client_secret=SECRET, redirect_uri=redirect)
    getPlayLists(token)
    getChoiceList(name_to_id[list(name_to_id.keys())[0]], token)
    lyri = getLyrics()


def authorize():
    auth = oauth2.SpotifyOAuth(client_id=C_ID, client_secret=SECRET, redirect_uri=redirect, scope=scoped, cache_path='.spotipyoauthcache')
    print(auth.get_authorize_url())


def getPlayLists(play_token):
    if play_token:
        sp = spotipy.Spotify(auth=play_token)

        # print(sp.user(username))
        results = sp.user_playlists(username)
        for i in results['items']:
            play_names.append(i['name'])
            name_to_id[i['name']] = i['id']

        return play_names

def getChoiceList(id, play_token):
    if play_token:
        sp = spotipy.Spotify(auth=play_token)
        list = sp.user_playlist_tracks(username, playlist_id=id, limit=10)

        # print(list)
        for song in list['items']:
            cur = []
            cur.append(song['track']['name'])
            for help in song['track']['artists']:
                if help['type'] == "artist":
                    cur.append(help['name'])
            arttitle.append(cur)

        # print(arttitle)



def getLyrics():
    all_lyrics = []
    f = open('lyrical.txt', "a+", encoding='utf-8')
    for item in arttitle:
        # print(item[0])
        data = {
            'q_track': item[0],
            'q_artist': item[1],
            'apikey': MMKEY,
            'format': 'json',
            's_track_rating': 'desc',
            'f_has_lyrics': 'true',
            'page_size':1,
        }

        res = req.get(mm_url + 'track.search', params=data)
        # print(res)
        # t =
        jres = json.loads(res.text)
        # print(jres)
        # print(jres['message']['body']['track_list'][0])
        try:
            short = jres['message']['body']['track_list'][0]

            track_id = short['track']['track_id']

            data2 = {
                'track_id': track_id,
                'apikey': MMKEY,
            }

            res2 = req.get(mm_url + 'track.lyrics.get', params=data2)
            jres2 = json.loads(res2.text)

            lyrics = jres2['message']['body']['lyrics']['lyrics_body'][:len(("...  ******* This Lyrics is NOT for Commercial use *******")]

            f.write(lyrics)


            all_lyrics.append(lyrics[:len("...  ******* This Lyrics is NOT for Commercial use *******")])


        except:
            continue



    f.close()
    return all_lyrics





runall()
