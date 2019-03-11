csv = '/Users/nathanoasis/PycharmProjects/SpotifyMSD/text/master_csv.csv'
genre_dict = {}
with open(csv, 'r') as file:
        for line in file:
                if line[0] is not '#':
                        line = line.rstrip()[::-1]
                        genre = line.split(',')[0][::-1]
                        if genre in genre_dict:
                                count = genre_dict[genre]
                                genre_dict[genre] = count + 1
                        else:
                                genre_dict[genre] = 1

# for k,v in genre_dict.items():
#        print k + ', ' + str(v)

d_view = [ (v,k) for k,v in genre_dict.items() ]
d_view.sort(reverse=True) # natively sort tuples by first element
# for v,k in d_view:
#     print "%s & %d \\\\" % (k,v)
print(d_view)