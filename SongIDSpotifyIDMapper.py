#########################################
# Created   : 2/27/19                   #
# Author    : Nathan Oasis              #
#########################################

# Importing library
import os
import json
#
walk_dir = "/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/millionsongdataset_echonest"
out_file_path = "/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/"
#
import time
start_time = time.time()


def get_song_info(song_info):
    song_info_str = ''
    song_id = song_info["id"]
    title = song_info["title"]
    artist_name = song_info["artist_name"]
    song_info_str += song_id + ',' + title + ',' + artist_name + ','
    return song_info_str


def parse_file(json_file_in_path):
    csv_string = ''
    with open(json_file_in_path) as jsonFile:
        inFile = json.load(jsonFile)

        song_info = get_song_info(inFile["response"]["songs"][0])
        csv_string += song_info

        tracks = inFile["response"]["songs"][0]["tracks"]

        for track in tracks:
            try:
                foreign_id = track["foreign_id"]
            except:
                print("could not get foreign_id for ", jsonFile)
            # getting the first spotify id. there are more than one.
            if foreign_id[:7] == "spotify":
                spotify_id = foreign_id[-22:]
                csv_string += spotify_id + ',\n'
                break
    return csv_string


with open(out_file_path + "convertedFiles.csv", "w") as convertedFiles:
    convertedFiles.write('song_id,title,artist,spotify_uri,\n')
    with open(out_file_path + "errorFiles.csv", "w") as errorFiles:
        parsed_count = 0
        error_count = 0
        for root, subdirs, files in os.walk(walk_dir):
            # print('--\nroot = ' + root)
            for filename in files:
                if filename.endswith(".json"):
                    file_path = os.path.join(root, filename) # filepath do the thing!!
                    # print('\t- file %s (full path: %s)' % (filename, file_path))
                    try:
                        parsed = parse_file(file_path)
                        convertedFiles.write(parsed)
                        parsed_count += 1
                    except:
                        errorFiles.write(filename[:-5] + ',\n')
                        error_count += 1
                        # print("could not parse ", file_path)
                if (parsed_count + error_count) % 100000 == 0:
                    print("completed", parsed_count + error_count, "files")
        print("parsed_count ", parsed_count)
        print("error_count", error_count)
        print("parsed", parsed_count/(parsed_count+error_count)*100, "% files")

print("--- %s seconds ---" % (time.time() - start_time))
print('walk_dir = ' + walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
