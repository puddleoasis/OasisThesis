#########################################
# Created   : 3/2/19                    #
# Author    : Nathan Oasis              #
#########################################

MSD_track_listing_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/unique_tracks.txt'
spotify_id_files_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/convertedFiles4.csv'
out_file_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/mergedIDs.csv'
out_file_path_unmerged = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/unmergedIDs.csv'
# dict_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/dict_temp.csv'


with open(MSD_track_listing_path, "r") as track_ids_file:
    with open(spotify_id_files_path, "r") as spotify_id_file:
        with open(out_file_path, "w") as outFile:
            with open(out_file_path_unmerged, "w") as errorFile:
                valid_mappings = 0
                invalid_mappings = 0
                outFile.write("MSD_track_id,spotify_uri,song_title,artist,\n")

                song_to_track_id = {}
                for line in track_ids_file:
                    data = line.split('<SEP>')
                    track_id = data[0]
                    song_id = data[1]
                    song_to_track_id[song_id] = track_id

                # with open(dict_path, 'w') as csv_file:
                #     for key, value in song_to_track_id.items():
                #         csv_file.write(key + ',' + value + ',\n')

                song_id_len = len('SOAAABI12A8C13615F')
                # i = 0
                # j = 0
                for line in spotify_id_file:
                    if line[0] is not '#':
                        song_id, rest_of_line = line[:song_id_len], line[song_id_len:]
                        try:
                            # i += 1
                            track_id = song_to_track_id[song_id]
                            outFile.write(track_id + rest_of_line)
                            valid_mappings += 1

                            # if i < 5:
                            #     print("healthy", song_id, " ", rest_of_line)
                        except:
                            # j += 1

                            errorFile.write(track_id + ',' + song_id + ',\n')
                            invalid_mappings += 1

                            # if j < 5:
                            #     print("unhealthy", song_id, " ", rest_of_line)

print("had", valid_mappings, "valid_mappings")
print("had", invalid_mappings, "invalid_mappings")
print(valid_mappings / (valid_mappings + invalid_mappings)*100, "% valid_mappings")