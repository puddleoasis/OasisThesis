file_dir = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MSD Benchmarks/CSV/Rhythm_Features/'

import os
#SOMETHING IS WRONG WITH THIS IDK WHY DONT USE THIS PROGRAM


# Getting all the arff files from the current directory
# files = [file for file in os.listdir(file_dir) if file.endswith(".csv")]

# files = ['Statistical_Spectrum_Descriptors.csv', 'Rhythm_Histograms.csv']
files = ['Rhythm_Histograms.csv']

for f in files:
    print(f)
    with open(file_dir+f, 'r') as reading:
        with open(file_dir+'1'+f, 'w') as writing:
            for i, line in enumerate(reading):
                line = line.rstrip().rstrip(',')
                if i == 0:
                    writing.write(','.join(line.split(',')[:-1]) + ',#track_id\n')
                else:
                    writing.write(line.rstrip(','))
                    
