import csv

ifile  = open('Student-2016-03-16.csv', "rb")
reader = csv.reader(ifile)

rownum = 0
for row in reader:
    print row
    print "-----------------"
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for col in row:
            print header[colnum],col
            colnum += 1
    print "################################"
    rownum += 1
ifile.close()