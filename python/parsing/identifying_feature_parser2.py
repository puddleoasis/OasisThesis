the_in_file = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/IDs_and_GenrePostParse.csv'
the_out_file = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/IDs_and_GenrePostPostParse.csv'
with open(the_in_file, 'r') as in_file:
    with open(the_out_file, 'w') as out_file:
        for line in in_file:
            the_line = line.split(',')
            out_file.write(the_line[0] + ',' + the_line[1] + ',' + the_line[-1])