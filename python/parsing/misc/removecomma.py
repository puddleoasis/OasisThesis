# file_dir = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MSD Benchmarks/CSV/Rhythm_Features/'

import os


# Getting all the arff files from the current directory
# files = [file for file in os.listdir(file_dir) if file.endswith(".csv")]

# files = ['Statistical_Spectrum_Descriptors.csv', 'Rhythm_Histograms.csv']
# files = ['Statistical_Spectrum_Descriptors.csv']

# file = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/spotify_features.csv'
file = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MSD Benchmarks/CSV/Rhythm_Features/Statistical_Spectrum_Descriptors.csv'
with open(file, 'r') as reading:
    with open(file[:-4]+'1.csv', 'w') as writing:
        for i, line in enumerate(reading):
            if i == 0:
                line = line.rstrip().split(',')
                updated_line = ','.join(['"SSD_'+v[1:] for v in line])
                updated_line = updated_line[:-14] + ',#track_id'
                writing.write(updated_line + '\n')
            else:
                writing.write(line)
                # line = line.rstrip().split(',')[::-1]
                # line = ','.join(line)
                # writing.write(line + '\n')
# ','.join(line[:-1])