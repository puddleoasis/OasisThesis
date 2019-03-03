# The objective of this class is to get all of the semantic data about all of the songs in that spotify user's 20 playlists.

import spotipy
import json

myToken = 'BQCOBdUTw93XyGNz5MGQnVT9X8cc026JspzmhAYh4Vzz1mwAfEdmzYiPOtzysgYiDMgOpuwnPjrGh_MUPmwZd8iI_ZNnYGLbm33hQEvB0X9QBleJemzIr-una221yNWLTkkDXAwXbguiuPuMX1zkJAAu_B0yz-EBud1slpqiove7uEa-'

sp = spotipy.Spotify(auth=myToken)

uri_file_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/merged_track_and_spotify/mergedIDs.csv'

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

# def writeToFile(data):
#     with open(out_file_path + 'SemanticFeatures', 'w') as out_file:


def get_uris(file_path):
    uris = []
    with open(file_path, "r") as uri_files:
        if


def main():
    spotify_uris = get_uris(uri_file_path)
    features = get_features_from_uris(spotify_uris)
    # features = getFeaturesFromURI(uris)
    # organizedfeatures = organizedObjs(features)
    # writeToFile(organizedfeatures)

main()
