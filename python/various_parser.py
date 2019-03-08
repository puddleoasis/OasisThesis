#########################################
# Created   : 2/27/19                   #
# Author    : Nathan Oasis              #
#########################################

# File used for various parsing.
import re

spotify_in_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/Semantic_Info/spotify_features.csv'
id_and_genre_in_path = '/Users/libuser/PycharmProjects/OasisThesis/text/merged_genre_id.csv'
out_file_path = '/Users/libuser/PycharmProjects/OasisThesis/text/master_csv.csv'

# def my_split(my_str):
#     split = []
#     quote_count = 0
#     for i, c in enumerate(my_str):
#         if c is '\"':
#             quote_count != 1
cc = 0

with open(spotify_in_path, "r") as spotify_file:
    genre_list = ['Pop_Rock', 'Electronic', 'Rap', 'Jazz', 'Latin', 'R&B', 'International', 'Country', 'Reggae',
                  'Blues', 'Vocal', 'Folk', 'New']
    features_dict = {}
    id_len = len('6i9aLGfG1Id1oCcpgmRjmE')
    for line in spotify_file:
        if line[0] is not '#':
            id = line[:id_len]
            features_dict[id] = line[:-2]
    # print(features_dict)

    # with open(id_and_genre_in_path, "r") as id_and_genre_file:
    #     with open(out_file_path, "w") as csv_file:
    #         for line in id_and_genre_file:
    #             if line[0] is not '#':
    #                 # split fields ignorign quotes.
    #                 data = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
    #                 spotify_id = data[3]
    #                 if len(spotify_id) is not id_len:
    #                     print(data)
    #                     print('\n' + data[-3] + '\n')
    #                 else:
    #                     cc += 1
    #                 try:
    #                     semantic_data_line = features_dict[spotify_id]
    #                     line.replace(spotify_id, semantic_data_line)
    #                     line = line[:-1]
    #                     csv_file.write(line)
    #                 except:
    #                     pass
    #                     # print('\nerror',spotify_id,'is not in dict..\n')
    #                     # print('data is',data)
    #         print('cc is', cc)
    with open(id_and_genre_in_path, "r") as id_and_genre_file:
        with open(out_file_path, "w") as csv_file:
            for line in id_and_genre_file:
                if line[0] is not '#':
                    try:
                        cpy = line[:-2]
                        rev = cpy[::-1]
                        # print(rev)
                        idx = rev.index(",")
                        # print('idx is',idx, len(line)-idx-id_len-1, idx-3)
                        # print('hi',line[len(line)-idx-id_len-3:len(line)-idx-3])
                        spotify_id = line[len(line)-idx-id_len-3:len(line)-idx-3]
                        # print('the', spotify_id)
                        semantic_data_line = features_dict[spotify_id]
                        line = line.replace(spotify_id, semantic_data_line)
                        line = line[:-1]
                        csv_file.write(line[:-1]+'\n')
                    except:
                        print(line[:-2])
