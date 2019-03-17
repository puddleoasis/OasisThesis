# The objective of this class is to get all of the semantic data about all of the songs in that spotify user's 20 playlists.

import spotipy
import json

myToken = 'BQBadsgqBgzz2OPnkt5wi5i1zjcXVPP0b-GKhyXaq-8O4BbpISOwO00nLYC8iGM0a0ZnCpO0kMN7_IL62Q0MmOrxu18TEwElV4Kq0XUES__bbYedPK7NyywFgX_i3fXu9uk8G7qhXs0y-FlfS0-LkZcRZU2ITNWjbpuESk_L_z1GMMUz'

sp = spotipy.Spotify(auth=myToken)

targetUser = 'bhavika'
targetPlaylistIDs = ['6f0QUSOezP5eBsaqbGcfhm', '78fZg3zrL9ra7MK8ogbw5o', '07cd841eYlduy8eQFoYfVU', '6iERYr736MfE3nrX716aLY', '78b1gPaRqiVwsjAa4Kf4X5', '6UjjRACBJn4twWyVCbdTSZ', '28vgvXIBgydwfVuKTeFbPd', '2WhfT5eDKn1IViLKRh31Hh', '38uhJMh7FwthRNNDR1a4r2', '6usaf2mG6xionTydmfhzRb', '4izebbDXU3mA3nBUpNRgPd', '3ybfE0Ls3SVxwe9xjuymxQ', '4lDMzQGJ0WTPZnarer1fvi', '2po6YXZgf1WQUPFFmhaMmz', '0y9uk8jUHMJseJkL6xDOXq', '7bZZSLc0dQlEj59tkcXXIb', '0Y1yyb3Uw1ixNFpiBGHHqO', '5Plzd6FBgKm0GcffCuoGZi', '0RVgirhL6ToF5GGGuks1Wh', '05UhiZt3EbWwO26mIpW6D2']



def get_artist_names_helper(artists_obj):
    names = []
    for artist in artists_obj:
        names.append(artist['name'])
    return names

def get_song_and_artist_name(tracks):
    track_data = []
    for t in tracks:
        try:
            song_name = t['track']['name']
        except:
            print('trying to get song name for ', t['track'])
        try:
            artist_name = get_artist_names_helper(t['track']['artists'])
        except:
            print('trying to get artist name for ', t['track']['artists'])
        tup = (song_name, artist_name)
        track_data.append(tup)
    return track_data


def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


def get_tracks_from_multiple_playlists(username, playlist_ids):
    results = []
    for playlist_id in playlist_ids:
        tracks = get_playlist_tracks(username, playlist_id)
        results.extend(tracks)
    return results


def writeToFile(data):
    with open('Track.json', 'w') as outfile:
        json.dump(data, outfile)

def main():
    # tracks = get_tracks_from_multiple_playlists(targetUser, targetPlaylistIDs)
    tracks = get_playlist_tracks(targetUser, targetPlaylistIDs[0])
    track_data  = get_song_and_artist_name(tracks)
    # print('total number of tracks is ', len(tracks))
    # uris = getURIfromTrack(tracks)
    # features = getFeaturesFromURI(uris)
    # organizedfeatures = organizedObjs(features)
    writeToFile(track_data)
    print('done')

main()
