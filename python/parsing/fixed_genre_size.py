songs_per_genre = 500

# dir = '/home/oasisn/Desktop/Thesis_CSVs/'
dir = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/out_files/'
RH_SSD = 'RH_SSD.csv'
RH_SSD_jMir_deriv = 'RH_SSD_jMir_deriv.csv'
RH_SSD_jMir_noderiv = 'RH_SSD_jMir_noderiv.csv'
RH_SSD_MARSYAS = 'RH_SSD_MARSYAS.csv'

files = [dir + RH_SSD_jMir_deriv, dir + RH_SSD_jMir_noderiv, dir + RH_SSD_MARSYAS, dir + RH_SSD]

genre_dict = {'Pop_Rock':set(), 'Electronic':set(), 'Rap':set(), 'Latin':set(),
          'Jazz':set(), 'International':set(), 'RnB':set(), 'Country':set(),
          'Blues':set(), 'Reggae':set(), 'Folk':set(), 'Vocal':set(), 'New':set()}

with open(files[0], 'r') as in_file:
    for i, line in enumerate(in_file):
        if i > 0:
            line = line.split(',')
            genre = line[-1].rstrip().lstrip('\"').rstrip('\"')
            msd_id = line[0]
            cnt_genre = len(genre_dict[genre])
            if cnt_genre < 500:
                genre_dict[genre].add(msd_id)

msd_ids = {x for v in genre_dict.values() for x in v}
print(len(msd_ids))
id_len = len('TRTQFGC128F422F013')


for feature_file in files:
    with open(feature_file, 'r') as in_file:
        with open(dir + 'eq_genre'+feature_file[len(dir):], 'w+') as out_file:
            for i, line in enumerate(in_file):
                if i == 0:
                    out_file.write(line)
                else:
                    msd_id = line[:id_len]
                    if msd_id in msd_ids:
                        out_file.write(line)
