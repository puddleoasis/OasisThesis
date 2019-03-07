# The objective of this class is to get all of the semantic data about all of the songs in that spotify user's 20 playlists.
# from spotipy import Spotify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# my_token = 'BQD_QOlDDIfRQU2-YP3xsRu1vXjxuMN_VDMZMyz_3AK9fbICAeKzod6mJLutZMEk55C4nejcBLGa7VpZ5fAvghEs_2TzL20H81_7e-cwwqiUh1FkvZqwh0afJBDkyAv1oZMd3x9ikh57jyLB6ryKj0F5J34Z_rKu2ZHyH8lNIor0JeFO'
# sp = Spotify()

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri_file_path = '/Users/nathanoasis/PycharmProjects/SpotifyMSD/text/mergedIDs.csv'
out_features_path = '/Users/nathanoasis/PycharmProjects/SpotifyMSD/text/spotify_features.csv'


def to_csv(fo):
    oo = str(fo['id']) + ',' + str(fo['danceability']) + ',' + str(fo['energy']) + ',' + str(
        fo['loudness']) + ',' + str(fo['speechiness']) + ',' + str(fo['acousticness']) + str(
        fo['instrumentalness']) + ',' + str(fo['liveness']) + ',' + str(fo['valence']) + ',' + str(
        fo['tempo']) + ',' + str(fo['key']) + ',\n'
    return oo


def get_features_from_uris(uris):
    features = []

    chunkSz = 50
    extra = len(uris) % chunkSz
    evenGroups = len(uris) - extra
    for i in range(0, evenGroups, chunkSz):
        features50 = sp.audio_features(uris[i: i + chunkSz])
        features.extend(features50)
        if i % 2000:
            print("done w 100,00 tracks")
    featuresRest = sp.audio_features(uris[-extra:])
    features.extend(featuresRest)

    return features


def organized_objs(featureObjs):
    objs = []
    for fo in featureObjs:
        csv_obj = to_csv(fo)
        objs.append(csv_obj)
    return objs


def get_uris(file_path):
    uris = []
    spotify_url_len = len('6i9aLGfG1Id1oCcpgmRjmE')
    with open(file_path, "r") as uri_files:
        for line in uri_files:
            if line[0] is not '#':
                uris.append(line[-spotify_url_len-2:-2])
    return uris



def writeToFile(data):
    with open(out_features_path, 'w') as out_file:
        out_file.write('spotify_id,danceability,energy,loudness,speechiness,acousticness,instrumentalness,liveness,valence,tempo,key,\n')
        for line in data:
            out_file.write(line)


def main():
    spotify_uris = get_uris(uri_file_path)
    print('got_uris')
    features = get_features_from_uris(spotify_uris)
    print('got_features')
    organized_features = organized_objs(features)
    print('organized_features')
    writeToFile(organized_features)
    print('wrote to file! done!')

main()
