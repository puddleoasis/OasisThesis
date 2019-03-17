# The objective of this class is to get song genre and mood information from the Rovi API.
# first we must get the Rovi IDs of the tracks we wish to get information for
# To get the IDs, we are using the Rovi search tool with the parameters of song title and artist name
# which were acquired from the MSDSubset db

import sqlite3

connection = sqlite3.connect('/Users/libuser/Downloads/MillionSongSubset 2/AdditionalFiles/subset_track_metadata.db')
cursor = connection.cursor()

sql_query = 'SELECT title, artist_name ' \
            'FROM songs'

cursor.execute(sql_query)

song_data = list(cursor.fetchall())

#############################################
##                                         ##
##  got all the song data (title, artist)  ##
##                                         ##
#############################################


for song in song_data:
    print(song)

