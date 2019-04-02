from string import ascii_lowercase
from string import ascii_uppercase
from string import digits

# file_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/IDs_and_GenrePostParse.csv'

acceptable_charset = set(ascii_lowercase + ascii_uppercase + digits)
all_chars = set()

with open(file_path, 'r') as in_file:
    for i, line in enumerate(in_file):
        if i == 0:
            print(line)
            for c in line:
                all_chars.add(c)

            print(list(all_chars - acceptable_charset))
        else:
            break
