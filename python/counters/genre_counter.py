csv = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/Building_CSV/FinalMaster2.csv'
genre_dict = {}
with open(csv, 'r') as file:
        for line in file:
                if line[0] is not '#':
                        genre = line.rstrip().split(',')[-1]
                        if genre in genre_dict:
                                count = genre_dict[genre]
                                genre_dict[genre] = count + 1
                        else:
                                genre_dict[genre] = 1
sum = 0
for k, v in sorted(genre_dict.iteritems(), key=lambda x: x[1], reverse=True):
        sum += v
        print k, v

print '\nTotal Count is', sum
