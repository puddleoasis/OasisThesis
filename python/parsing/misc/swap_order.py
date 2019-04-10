dir = '/home/oasisn/Desktop/Thesis_CSVs/'
RH_SSD = 'eq_genreRH_SSD.csv'
RH_SSD_jMir_deriv = 'eq_genreRH_SSD_jMir_deriv.csv'
RH_SSD_jMir_noderiv = 'eq_genreRH_SSD_jMir_noderiv.csv'
RH_SSD_MARSYAS = 'eq_genreRH_SSD_MARSYAS.csv'

files = [dir + RH_SSD_jMir_deriv, dir + RH_SSD_jMir_noderiv, dir + RH_SSD_MARSYAS, dir + RH_SSD]


for file in files:
    with open(file, 'r') as inFile:
        with open(file.rstrip('.csv') + '2.csv', 'w') as outFile:
            for line in inFile:
                line = line.split(',')
                new_line = line[0] + ',' + ','.join(line[2:])
                outFile.write(new_line)

                # line = line.rstrip()[:-1].split(',')
                # a = line[0]
                # b = ','.join(line[1:-1])
                # c = line[-1]
                # outFile.write(a + ',' + c + ',' + b + '\n')
