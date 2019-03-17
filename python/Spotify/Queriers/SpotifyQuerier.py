# The objective of this class is to get all of the semantic data about all of the songs in that spotify user's 20 playlists.
# from spotipy import Spotify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# my_token = 'BQAYO8UZ1WsATNWkGixbpyE85qtJ2mZrkA1qE9_kFKdgC8br2AxnFR0cpS6EA9kp__ainFnzsyTyhKtGa1shN19gOhfrUWdkTRgao-tS9NJsrvM_q85mFjPfDlIuWkdMh7dmEfmkZ4dUsxIqdy5bLrluXlrYhfSjq9WHSM2ILIKhk3nX'
# sp = Spotify()
client_id = '8be5e7ba3c2f49ca9b71969ac7b686f0'
client_secret = 'b9a168382c594ce1b142be1a313c386c'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri_file_path = '/Users/libuser/PycharmProjects/OasisThesis/text/IDs_and_Genre.csv'
out_features_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/Semantic_Info/spotify_features.csv'
failed_out_features_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/Semantic_Info/failed_spotify_uris.csv'


def to_csv(fo):
    try:
        oo = str(fo['id']) + ',' + str(fo['danceability']) + ',' + str(fo['energy']) + ',' + str(
            fo['loudness']) + ',' + str(fo['speechiness']) + ',' + str(fo['acousticness']) + ',' + str(
            fo['instrumentalness']) + ',' + str(fo['liveness']) + ',' + str(fo['valence']) + ',' + str(
            fo['tempo']) + ',' + str(fo['key']) + '\n'
        return oo
    except ValueError as e:
        return str(fo['id'])


def get_features_from_uris(uris):
    chunkSz = 50
    extra = len(uris) % chunkSz
    evenGroups = len(uris) - extra
    with open(out_features_path, 'w') as out_file_temp:
        out_file_temp.write('spotify_id,danceability,energy,loudness,speechiness,acousticness,instrumentalness,liveness,valence,tempo,key\n')
        for i in range(0, evenGroups, chunkSz):
            features50 = sp.audio_features(uris[i: i + chunkSz])
            organized_features = organized_objs(features50)
            for feature in organized_features:
                out_file_temp.write(feature)
        featuresRest = sp.audio_features(uris[-extra:])
        organized_features = organized_objs(featuresRest)
        for feature in organized_features:
            out_file_temp.write(feature)

    # return features


def organized_objs(featureObjs):
    objs = []
    for fo in featureObjs:
        if fo is not None:
            csv_obj = ''
            try:
                csv_obj = to_csv(fo)
            except:
                with open(failed_out_features_path, 'w') as failed:
                    failed.write(fo['id']+',\n')
            objs.append(csv_obj)
    return objs


def get_uris(file_path):
    uris = []
    with open(file_path, "r") as uri_files:
        for line in uri_files:
            if line[0] is not '#':
                uri = line.split(',')[1]
                uris.append(uri)
    return uris


def writeToFile(data):
    with open(out_features_path, 'w') as out_file:
        out_file.write('spotify_id,danceability,energy,loudness,speechiness,acousticness,instrumentalness,liveness,valence,tempo,key,\n')
        for line in data:
            out_file.write(line)


def main():
    spotify_uris = get_uris(uri_file_path)
    print('got_uris')
    # features = get_features_from_uris(spotify_uris)
    get_features_from_uris(spotify_uris)
    # print('got_features')
    # organized_features = organized_objs(features)
    # print('organized_features')
    # writeToFile(organized_features)
    # print('wrote to file! done!')

main()
