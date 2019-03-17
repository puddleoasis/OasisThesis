file_path = '/Users/libuser/PycharmProjects/OasisThesis/text/mergedSpotifyandTrackIDs.csv'
file_out_path = '/Users/libuser/PycharmProjects/OasisThesis/text/mergedSpotifyandTrackIDs2.csv'

with open(file_path, 'r') as inFile:
    with open(file_out_path, 'w') as outFile:
        for i, line in enumerate(inFile):
            line = line.rstrip()[:-1].split(',')
            a = line[0]
            b = ','.join(line[1:-1])
            c = line[-1]
            outFile.write(a + ',' + c + ',' + b + '\n')
