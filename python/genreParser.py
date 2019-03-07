#########################################
# Created   : 2/27/19                   #
# Author    : Nathan Oasis              #
#########################################

# Importing library

genre_in_path = '/Users/nathanoasis/PycharmProjects/SpotifyMSD/TOP-genreAssignment.txt'
merged_id_path = '/Users/nathanoasis/PycharmProjects/SpotifyMSD/mergedIDs.csv'
merged_id_genre_path = '/Users/nathanoasis/PycharmProjects/SpotifyMSD/'
failed_tracks_path = '/Users/nathanoasis/PycharmProjects/SpotifyMSD/'

with open(genre_in_path, "r") as genre_file:
    track_id_to_genre = {}
    for line in genre_file:
        data = line.split()
        track_id_to_genre[data[0]] = data[1]
    with open(merged_id_path, "r") as id_file:
        with open(merged_id_genre_path + 'merged_genre_id.csv', "w") as outFile:
            with open(merged_id_genre_path + 'failed_merged_genre_id.csv', "w") as failedOutFile:
                outFile.write("track_id,song_title,artist,spotify_id,genre,\n")

                track_id_len = len('TRMTUKT12903CEE7C3')
                success = 0
                error = 0
                for line in id_file:
                    if line[0] is not '#':
                        track_id = line[:track_id_len]
                        try:
                            track_genre = track_id_to_genre[track_id]
                            outFile.write(line.rstrip() + track_genre + ',\n')
                            success += 1
                        except:
                            failedOutFile.write(track_id + '\n')
                            error += 1

print('success', success)
print('error', error)
print('percentage is', success/(success+error)*100)
