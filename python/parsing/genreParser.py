#########################################
# Created   : 2/27/19                   #
# Author    : Nathan Oasis              #
#########################################

# Importing library

genre_in_path = '/Users/libuser/PycharmProjects/OasisThesis/text/assignment/TrackID_Top-Genre.txt'
merged_id_path = '/Users/libuser/PycharmProjects/OasisThesis/text/mergedSpotifyandTrackIDs.csv'
out_path_success = '/Users/libuser/PycharmProjects/OasisThesis/text/IDs_and_Genre.csv'
out_path_failed = '/Users/libuser/PycharmProjects/OasisThesis/text/Failed_IDs_and_Genre.csv'

with open(genre_in_path, "r") as genre_file:
    track_id_to_genre = {}
    for line in genre_file:
        data = line.split()
        track_id_to_genre[data[0]] = data[1]
    with open(merged_id_path, "r") as id_file:

        with open(out_path_success, "w") as outFile:
            with open(out_path_failed, "w") as failedOutFile:
                outFile.write("#track_id,spotify_id,song_title,artist,genre\n")

                track_id_len = len('TRMTUKT12903CEE7C3')
                success = 0
                error = 0
                for line in id_file:
                    if line[0] is not '#':
                        track_id = line[:track_id_len]
                        try:
                            track_genre = track_id_to_genre[track_id]
                            outFile.write(line.rstrip() + ',' + track_genre + '\n')
                            success += 1
                        except:
                            failedOutFile.write(track_id + '\n')
                            error += 1

print('success', success)
print('error', error)
print('percentage is', success/(success+error)*100)
