# Importing library
import os

# Getting all the arff files from the current directory
in_file_path = "/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MSD Benchmarks/CSV_Subset/subset_unique_tracks.csv"
out_file_path = "/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MSD Benchmarks/CSV_Subset/subset_unique_tracks2.csv"

track_id_length = len("TRBIHGD128F92E8D12")


# Main loop for reading and writing files
with open(in_file_path, "r") as inFile:
    with open(out_file_path, "w") as outFile:
        for line in inFile:
            outFile.write("\'"+line[:track_id_length] + "\',\n")