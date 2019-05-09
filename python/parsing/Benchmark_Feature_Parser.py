#########################################
# Created   : 3/16/19                   #
# Author    : Nathan Oasis              #
#########################################

# Paths
# error_id_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/no_structal_features.csv'

low_level_feature_dir = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MSD Benchmarks/CSV/Low-Level_Features/'
mid_level_feature_dir = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MSD Benchmarks/CSV/Rhythm_Features/'

AoM = low_level_feature_dir + 'Area_of_Moments.csv'
MoM = low_level_feature_dir + 'Method_of_Moments.csv'
LPC = low_level_feature_dir + 'Linear_Predictive_Coding.csv'
MFCC = low_level_feature_dir + 'MFCC.csv'
Spec_All = low_level_feature_dir + 'Spectral_All.csv'
Spec_All_Deriv = low_level_feature_dir + 'Spectral_All_Derivatives.csv'
Marsyas = low_level_feature_dir + 'Marsyas_Timbral.csv'
RH = mid_level_feature_dir + 'Rhythm_Histograms.csv'
SSD = mid_level_feature_dir + 'Statistical_Spectrum_Descriptors.csv'
Spotify = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/spotify_features.csv'
feature_dicts = {Spotify: {}, AoM: {}, MoM: {}, LPC: {}, MFCC: {}, Spec_All: {}, Spec_All_Deriv: {}, Marsyas: {}, RH: {}, SSD: {}}
features = ['AoM', 'MoM', 'LPC', 'MFCC', 'Spec_All', 'Spec_All_Deriv', 'Marsyas', 'RH', 'SSD', 'Spotify']

out_dir = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/CSV_Partitions/'
# feat = [('AoM', {AoM}), ('MoM', {MoM}), ('LPC', {LPC}), ('MFCC', {MFCC}), ('Spec_All', {Spec_All}),
#         ('Spec_All_Deriv', {Spec_All_Deriv}), ('Marsyas', {Marsyas}), ('RH', {RH}), ('SSD', {SSD}),
#         ('Spotify', {Spotify}), ('RH_SSD_jMir_deriv', {RH, SSD, AoM, MoM, LPC, MFCC, Spec_All_Deriv}),
#         ('RH_SSD_jMir_noderiv', {RH, SSD, AoM, MoM, LPC, MFCC, Spec_All}),
#         ('RH_SSD_MARSYAS', {RH, SSD, Marsyas}), ('RH_SSD', {RH, SSD}), ('ALL', {RH, SSD, Marsyas, Spotify})]
feat = [('MARSYAS_Spotify', {Marsyas, Spotify}), ('RH_Spotify', {RH, Spotify}), ('SSD_Spotify', {SSD, Spotify}),
        ('jMir_deriv_Spotify', {AoM, MoM, LPC, MFCC, Spec_All_Deriv}), ('LPC_Spotify', {LPC, Spotify}), ('MoM_Spotify', {MoM, Spotify}),
        ('ALL', {RH, SSD, AoM, MoM, LPC, MFCC, Spec_All, Spec_All_Deriv, Marsyas, Spotify})]
out_files = {out_dir + featname + '.csv': path for featname, path in feat}
print(out_files)


master_cvs_IN_PATH = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/IDs_and_Genre.csv'

msd_track_ids_included = set()
spotify_track_ids_included = set()
with open(master_cvs_IN_PATH, "r") as master_IN:
    for line in master_IN:
        split = line.split(',')  # spotify is 1. track is 0.
        msd_id = split[0]
        spotify_id = split[1]
        msd_track_ids_included.add(msd_id)
        spotify_track_ids_included.add(spotify_id)

for feature in feature_dicts:
    print('Working on building dict for feature file', feature)
    with open(feature, 'r') as feature_file:
        for line in feature_file:
            line = line.rstrip().rstrip(',').split(',')
            feature_id = line[-1].lstrip('\'').rstrip('\'')

            if feature is Spotify:
                if feature_id in spotify_track_ids_included:
                    feature_dicts[feature][feature_id] = ','.join(line[:-1])
            else:
                if feature_id in msd_track_ids_included:
                    feature_dicts[feature][feature_id] = ','.join(line[:-1])

with open(master_cvs_IN_PATH, "r") as master_IN:
    for out_file in out_files:
        included_feature_paths = out_files[out_file]

        with open(out_file, "w") as the_out_file:
            print('writing to', the_out_file)
            exceptions = 0
            for line in master_IN:
                line = line.split(',')
                msd_id = line[0]
                spotify_id = line[1]

                idstxt = ','.join(line[:-1]) + ','
                genre = line[-1]

                feature_str = ''
                try:
                    for feature_key in included_feature_paths:
                        if feature_key == Spotify:
                            feature_str += (feature_dicts[feature_key][spotify_id] + ',')
                        else:
                            feature_str += (feature_dicts[feature_key][msd_id] + ',')
                    # spot_features = feature_dicts[Spotify][spotify_id]
                    # spot_features = '' + ','
                    # spot_features = ''
                    # s = idstxt + ',' + feature_str + spot_features + genre
                    s = idstxt + feature_str + genre
                    the_out_file.write(s)
                except:
                    exceptions += 1
                    pass  # could write to error file here...
            print('found', exceptions, 'exceptions')
            master_IN.seek(0)
