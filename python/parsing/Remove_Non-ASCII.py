import re
# pattern = re.compile('([\W]|[\S])+')
# pattern = re.compile('([\w\s])+')
pattern = re.compile('[^\w ]')

cvs_IN_PATH = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/IDs_and_Genre.csv'
cvs_OUT_PATH = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/IDs_and_GenrePostParse.csv'


with open(cvs_IN_PATH, 'r') as in_file:
    with open(cvs_OUT_PATH, 'w') as out_file:
        for i, line in enumerate(in_file):
            if i == 5:
                data = line.rstrip().split(',')
                first = ','.join(data[:2])
                genre = '\"' + data[-1] + '\"'

                middle = data[2:-1]
                print(middle)
                song = '\"' + pattern.sub('', middle[0]) + '\"'
                artist = '\"' + pattern.sub('', middle[1]) + '\"'

                s = first + ',' + song + ',' + artist + ',' + genre + '\n'
                out_file.write(s)