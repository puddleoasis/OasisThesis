from string import ascii_lowercase
from string import ascii_uppercase
from string import digits

file_path = '/Users/nathanoasis/PycharmProjects/SpotifyMSD/text/IDs_and_Genre.csv'
#
acceptable_charset = set(ascii_lowercase + ascii_uppercase + digits)
all_chars = set()

with open(file_path, 'r') as in_file:
    for line in in_file:
        for c in line:
            all_chars.add(c)

print(list(all_chars - acceptable_charset))
