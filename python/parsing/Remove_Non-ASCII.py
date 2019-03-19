import re
# pattern = re.compile('([\W]|[\S])+')
# pattern = re.compile('([\w\s])+')
pattern = re.compile('[^\w ]')

cvs_IN_PATH = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/FinalMaster.csv'
cvs_OUT_PATH = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/FinalMaster2.csv'


with open(cvs_IN_PATH, 'r') as in_file:
    with open(cvs_OUT_PATH, 'w') as out_file:
        for line in in_file:
            data = line.rstrip().split(',')
            first = ','.join(data[:2])
            end = ','.join(data[-554+3:-1])
            genre = '\"' + data[-1] + '\"'

            middle = data[2:-554+3]
            song = '\"' + pattern.sub('', middle[0]) + '\"'
            artist = '\"' + pattern.sub('', middle[1]) + '\"'

            s = first + ',' + song + ',' + artist + ',' + end + ',' + genre
            out_file.write(s)