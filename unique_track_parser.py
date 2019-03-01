#########################################
# Created   : 2/27/19                   #
# Author    : Nathan Oasis              #
#########################################

# Importing library

in_file_path = "/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/unique_tracks.txt"
out_file_path = "/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/unique_tracks.csv"

with open(in_file_path, "r") as inFile:
    with open(out_file_path, "w") as outFile:
        outFile.write("track_id, song_id, song_title, artist,\n")
        for line in inFile:
            data = line.split("<SEP>")
            outFile.write(data[0] + "," + data[1] + "," + data[3].strip('\n') + "," + data[2] + ",\n")
