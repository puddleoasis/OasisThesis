import re

pattern = re.compile('[^\w ]')

# cvs_IN_PATH = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/IDs_and_Genre.csv'
# cvs_OUT_PATH = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/IDs_and_GenrePostParse.csv'
cvs_IN_PATH = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/MasterUnparsed.csv'
cvs_OUT_PATH = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/MasterParsed.csv'


cols = 1571 - 4
with open(cvs_IN_PATH, 'r') as in_file:
    with open(cvs_OUT_PATH, 'w') as out_file:
        for i, line in enumerate(in_file):
            if i == 5:
                data = line.rstrip().split(',')
                print(len(data))
                print(data[:-cols])
                first = ','.join(data[:2])
                middle = data[2:-cols]
                end = ','.join(data[:-cols])
                # genre = '\"' + data[-1] + '\"'

                print(middle)
                song = ','.join(middle[:-1])
                print(song)
                artist = middle[-1]
                song = '\"' + pattern.sub('', song) + '\"'
                artist = '\"' + pattern.sub('', artist) + '\"'

                s = first + ',' + song + ',' + artist + ',' + end + '\n'
                out_file.write(s)