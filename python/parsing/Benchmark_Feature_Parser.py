#########################################
# Created   : 3/16/19                   #
# Author    : Nathan Oasis              #
#########################################

# Importing library
master_cvs_IN_PATH = '/Users/libuser/PycharmProjects/OasisThesis/text/IDs_and_Genre.csv'
master_cvs_OUT_PATH = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/merge_testing1.csv'
# low_level_feature_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MSD Benchmarks/CSV/Low-Level_Features/Method_of_Moments.csv'
# low_level_feature_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MSD Benchmarks/CSV/Low-Level_Features/Spectral_All.csv'
low_level_feature_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MSD Benchmarks/CSV/Rhythm_Features/Rhythm_Histograms.csv'
error_id_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/no_structal_features.csv'
# import os
#
# # Getting all the arff files from the current directory
# files = [arff for arff in os.listdir('.') if arff.endswith(".arff")]


track_ids_included = set()
with open(master_cvs_IN_PATH, "r") as master_IN:
    for line in master_IN:
        id = line.split(',')[0]
        track_ids_included.add(id)
    print(len(track_ids_included))

feature_map = {}
with open(low_level_feature_path, "r") as feature_path:
    for line in feature_path:
        line = line.rstrip().rstrip(',').split(',')
        feature_id = line[-1].lstrip('\'').rstrip('\'')
        if feature_id in track_ids_included:
            feature_map[feature_id] = ','.join(line[:-1])
    print(len(feature_map))

with open(master_cvs_IN_PATH, "r") as master_IN:
    with open(master_cvs_OUT_PATH, "w") as outFile:
        for line_in in master_IN:
            line_in = line_in.split(',')
            line_id = line_in[0]
            if line_id in feature_map:
                feature_line = feature_map[line_id]
                first_bit = ','.join(line_in[:-1])
                genre = line_in[-1]
                combined_line = first_bit + ',' + feature_line + ',' + genre
                outFile.write(combined_line)
            else:
                with open(error_id_path, 'w') as errorFile:
                    errorFile.write(line_id + '\n')


