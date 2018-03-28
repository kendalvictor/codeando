import csv

print "Ingrese nombre de csv: ",
name = raw_input()
name_csv = name + '.csv'
f = open(name_csv, 'w')

ww = csv.writer(f,delimiter=',')
for x in range(0,11):
    ww.writerow((x*2, x*3, x*4,))
f.close()

