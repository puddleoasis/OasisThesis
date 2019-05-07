songs_per_genre = 500

# dir = '/home/oasisn/Desktop/Thesis_CSVs/'
dir = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/CSV_Partitions/All_Instances/'
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


# files = [dir + RH_SSD_jMir_deriv, dir + RH_SSD_jMir_noderiv, dir + RH_SSD_MARSYAS, dir + RH_SSD, dir + Spotify]
# files = ['eq_genre'+x for x in files]

genre_dict = {'Pop_Rock':set(), 'Electronic':set(), 'Rap':set(), 'Latin':set(),
          'Jazz':set(), 'International':set(), 'RnB':set(), 'Country':set(),
          'Blues':set(), 'Reggae':set(), 'Folk':set(), 'Vocal':set(), 'New':set()}

# genre_dict = {'Pop_Rock':set(), 'Electronic':set(), 'Rap':set(),
#               'Country':set(), 'Reggae':set(), 'New':set()}

for file in files:
    with open(file, 'r') as in_file:
        for i, line in enumerate(in_file):
            if i > 0:
                line = line.split(',')
                if 'Spotify' not in file:
                    genre = line[-1].rstrip().lstrip('\"').rstrip('\"')
                    # print(genre)
                else:
                    genre = line[-1].rstrip()
                    # print(genre)
                if genre in genre_dict: # this is for the restricted genres...6.
                    msd_id = line[0]
                    cnt_genre = len(genre_dict[genre])
                    if cnt_genre < 500:
                        genre_dict[genre].add(msd_id)

msd_ids = {x for v in genre_dict.values() for x in v}
print(len(msd_ids))
id_len = len('TRTQFGC128F422F013')


for feature_file in files:
    with open(feature_file, 'r') as in_file:
        with open(dir + 'eq_genre13'+feature_file[len(dir):], 'w+') as out_file:
            print('working on out file', feature_file)
            for i, line in enumerate(in_file):
                if i == 0:
                    out_file.write(line)
                else:
                    msd_id = line[:id_len]
                    if msd_id in msd_ids:
                        out_file.write(line)
