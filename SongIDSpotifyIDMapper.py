#########################################
# Created   : 2/27/19                   #
# Author    : Nathan Oasis              #
#########################################

# Importing library
# import os
import json
#
# root_path = "/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/millionsongdataset_echonest"
# out_file_path = "/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials"
#
# # for each file in lower directory
# for path, subdirs, files in os.walk(root_path):
#     for name in files:
#         print os.path.join(path, name)


##JSON PARSING
json_file_in_path = "/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/temp/SOAAZZH12A58A7F63.json"
csv_file_out_path = "/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/temp/SOAAZZH12A58A7F63.csv"
def parse_file(json_file_in_path):
    with open(json_file_in_path) as jsonFile:
        with open(csv_file_out_path, "w") as CSVFile:
            inFile = json.load(jsonFile)

            song_info = inFile["response"]["songs"][0]

            song_id = song_info["id"]
            title = song_info["title"]
            artist_name = song_info["artist_name"]
            CSVFile.write(song_id + "," + title + "," + artist_name + ",")

            tracks = inFile["response"]["songs"][0]["tracks"]
            for track in tracks:
                foreign_id = track["foreign_id"]
                # getting the first spotify id. there are more than one.
                if foreign_id[:7] == "spotify":
                    spotify_id = foreign_id[-22:]
                    CSVFile.write(spotify_id + ",\n")
                    break

