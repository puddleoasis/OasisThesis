# The objective of this class is to get all of the semantic data about all of the songs in that spotify user's 20 playlists.

import spotipy
import json

myToken = 'BQCOBdUTw93XyGNz5MGQnVT9X8cc026JspzmhAYh4Vzz1mwAfEdmzYiPOtzysgYiDMgOpuwnPjrGh_MUPmwZd8iI_ZNnYGLbm33hQEvB0X9QBleJemzIr-una221yNWLTkkDXAwXbguiuPuMX1zkJAAu_B0yz-EBud1slpqiove7uEa-'

sp = spotipy.Spotify(auth=myToken)


# targetUser = 'bhavika'
# targetPlaylistIDs = ['6f0QUSOezP5eBsaqbGcfhm', '78fZg3zrL9ra7MK8ogbw5o', '07cd841eYlduy8eQFoYfVU', '6iERYr736MfE3nrX716aLY', '78b1gPaRqiVwsjAa4Kf4X5', '6UjjRACBJn4twWyVCbdTSZ', '28vgvXIBgydwfVuKTeFbPd', '2WhfT5eDKn1IViLKRh31Hh', '38uhJMh7FwthRNNDR1a4r2', '6usaf2mG6xionTydmfhzRb', '4izebbDXU3mA3nBUpNRgPd', '3ybfE0Ls3SVxwe9xjuymxQ', '4lDMzQGJ0WTPZnarer1fvi', '2po6YXZgf1WQUPFFmhaMmz', '0y9uk8jUHMJseJkL6xDOXq', '7bZZSLc0dQlEj59tkcXXIb', '0Y1yyb3Uw1ixNFpiBGHHqO', '5Plzd6FBgKm0GcffCuoGZi', '0RVgirhL6ToF5GGGuks1Wh', '05UhiZt3EbWwO26mIpW6D2']


def organizeObj(fo):

    d = {
            fo['id']:
        (
            {'danceability':      fo['danceability']},
            {'energy':            fo['energy']},
            {'loudness':          fo['loudness']},
            {'speechiness':       fo['speechiness']},
            {'acousticness':      fo['acousticness']},
            {'instrumentalness':  fo['instrumentalness']},
            {'liveness':          fo['liveness']},
            {'valence':           fo['valence']},
            {'tempo':             fo['tempo']},
            {'key':               fo['key']}
        )
    }
    return d


def getFeaturesFromURI(uris):
    features = []

    chunkSz = 50
    extra = len(uris) % chunkSz
    evenGroups = len(uris) - extra
    for i in range(0, evenGroups, chunkSz):
        features50 = sp.audio_features(uris[i: i + chunkSz])
        features.extend(features50)
    featuresRest = sp.audio_features(uris[-extra:])
    features.extend(featuresRest)

    return features


def organizedObjs(featureObjs):
    objs = []
    for fo in featureObjs:
        # oo = organizeObj(fo)
        objs.append(oo)
    return objs


def getURIfromTrack(tracks):
    uris = []
    for t in tracks:
        uri = t['track']['uri'][-22:]
        uris.append(uri)
    return uris

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
    with open('SpotifyData.json', 'w') as outfile:
        json.dump(data, outfile)

def main():
    tracks = get_tracks_from_multiple_playlists(targetUser, targetPlaylistIDs)
    # print('total number of tracks is ', len(tracks))
    uris = getURIfromTrack(tracks)
    features = getFeaturesFromURI(uris)
    organizedfeatures = organizedObjs(features)
    writeToFile(organizedfeatures)

main()
