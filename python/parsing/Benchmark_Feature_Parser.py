#########################################
# Created   : 3/16/19                   #
# Author    : Nathan Oasis              #
#########################################

# Importing library
import os
import tempfile

# Vars
# SEARCH_ON_ID = 0 # search on MSD id
SEARCH_ON_ID = 1 # search on spotify id

# Paths
# master_cvs_IN_PATH = '/Users/libuser/PycharmProjects/OasisThesis/text/IDs_and_Genre.csv'
# master_cvs_OUT_PATH = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/Master.csv'
error_id_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/no_structal_features.csv'

low_level_feature_dir = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MSD Benchmarks/CSV/Low-Level_Features/'
low_level_feature_paths = [low_level_feature_dir+file for file in os.listdir(low_level_feature_dir) if file.endswith(".csv")]

timbral_features = ['/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MSD Benchmarks/CSV/Timbral_Features/Marsyas_Timbral.csv']

mid_level_feature_dir = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MSD Benchmarks/CSV/Rhythm_Features/'
mid_level_feature_file1 = 'Rhythm_Histograms.csv'
mid_level_feature_file2 = 'Statistical_Spectrum_Descriptors.csv'
mid_level_feature_paths = [mid_level_feature_dir+mid_level_feature_file1, mid_level_feature_dir+mid_level_feature_file2]


master_cvs_IN_PATH = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/Master01234567.csv'
master_cvs_OUT_PATH = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/FinalMaster2.csv'

feature_paths = ['/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/spotify_features.csv']
# feature_paths = []
# feature_paths.extend(low_level_feature_paths)
# feature_paths.extend(mid_level_feature_paths)
# feature_paths.extend(timbral_features)

track_ids_included = set()
with open(master_cvs_IN_PATH, "r") as master_IN:
    for line in master_IN:
        id = line.split(',')[SEARCH_ON_ID] # spotify is 1. track is 0.
        track_ids_included.add(id)
    print(len(track_ids_included))

i = 0

with open(error_id_path, 'w') as errorFile:
    for feature_path in feature_paths:
        print('Working on feature file', feature_path)

        feature_map = {}
        with open(feature_path, "r") as feature_file:
            for line in feature_file:
                line = line.rstrip().rstrip(',').split(',')
                feature_id = line[-1].lstrip('\'').rstrip('\'')
                if feature_id in track_ids_included:
                    feature_map[feature_id] = ','.join(line[:-1])

        with open(master_cvs_IN_PATH, "r") as master_IN:
            with open(master_cvs_OUT_PATH, "w") as outFile:
                for line_in in master_IN:
                    line_in = line_in.split(',')
                    line_id = line_in[SEARCH_ON_ID]
                    if line_id in feature_map:
                        feature_line = feature_map[line_id]
                        first_bit = ','.join(line_in[:-1])
                        genre = line_in[-1]
                        combined_line = first_bit + ',' + feature_line + ',' + genre
                        outFile.write(combined_line)
                    else:
                        errorFile.write(line_id + '\n')

        master_cvs_IN_PATH = master_cvs_OUT_PATH
        master_cvs_OUT_PATH = master_cvs_OUT_PATH[:-4] + str(i) + '.csv'
        i += 1
