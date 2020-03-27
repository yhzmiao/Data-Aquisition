fin = open("date.txt", 'r')
dates = fin.readlines()

fout = open("go.sh", 'w')
for i in range(0, len(dates) - 1):
	print >> fout, 'echo Now for ' + dates[i][:-1] + '!'
	print >> fout, 'python Exporter.py --querysearch \"Hummer\" --since ' + dates[i][:-1] + ' --until ' + dates[i + 1][:-1]
	print >> fout, 'cp output_got.csv Hummer/' + dates[i][2:-1] + '.csv'
