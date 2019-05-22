songs_per_genre = 2000

# dir = '/home/oasisn/Desktop/Thesis_CSVs/'
dir = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/CSV_Partitions/poster_pass/'
# RH_SSD = 'RH_SSD.csv'
# RH_SSD_jMir_deriv = 'RH_SSD_jMir_deriv.csv'
# RH_SSD_jMir_noderiv = 'RH_SSD_jMir_noderiv.csv'
# RH_SSD_MARSYAS = 'RH_SSD_MARSYAS.csv'
# Spotify = 'Spotify.csv'

from os import listdir


def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ dir + filename for filename in filenames if filename.endswith( suffix ) ]


files = find_csv_filenames(dir)
print(files)


# files = [dir + RH_SSD_jMir_deriv, dir + RH_SSD_jMir_noderiv, dir + RH_SSD_MARSYAS, dir + RH_SSD, dir + Spotify]
# files = ['eq_genre'+x for x in files]

# genre_dict1 = {'Pop_Rock':set(), 'Electronic':set(), 'Rap':set(), 'Latin':set(),
#           'Jazz':set(), 'International':set(), 'RnB':set(), 'Country':set(),
#           'Blues':set(), 'Reggae':set(), 'Folk':set(), 'Vocal':set(), 'New':set()}

# genre_dict2 = {'Pop_Rock':set(), 'Electronic':set(), 'Rap':set(),
#               'Country':set(), 'Reggae':set(), 'New':set()}

genre_dict2 = {'Pop_Rock':set(), 'Country':set()}

for file in files:
    with open(file, 'r') as in_file:
        for i, line in enumerate(in_file):
            if i > 0:
                line = line.split(',')
                genre = line[-1].rstrip().lstrip('\"').rstrip('\"')

                # if genre in genre_dict1: # this is for the restricted genres...6.
                #     msd_id = line[0]
                #     cnt_genre = len(genre_dict1[genre])
                #     if cnt_genre < songs_per_genre:
                #         genre_dict1[genre].add(msd_id)
                if genre in genre_dict2: # this is for the restricted genres...6.
                    msd_id = line[0]
                    cnt_genre = len(genre_dict2[genre])
                    if cnt_genre < songs_per_genre:
                        genre_dict2[genre].add(msd_id)

# msd_ids1 = {x for v in genre_dict1.values() for x in v}
msd_ids2 = {x for v in genre_dict2.values() for x in v}
# print(len(msd_ids1))
print(len(msd_ids2))

for feature_file in files:
    with open(feature_file, 'r') as in_file:
        # with open(dir + 'eq_genre13'+feature_file[len(dir):], 'w+') as out_file1:
            with open(dir + 'eq_genre2' + feature_file[len(dir):], 'w+') as out_file2:
                print('working on out file', feature_file)
                for i, line in enumerate(in_file):
                    line = line.split(',')
                    msd_id = line[0]
                    line = ','.join(line[2:])
                    if i == 0:
                        # out_file1.write(line)
                        out_file2.write(line)
                    else:
                        # if msd_id in msd_ids1:
                        #     out_file1.write(line)
                        if msd_id in msd_ids2:
                            out_file2.write(line)
