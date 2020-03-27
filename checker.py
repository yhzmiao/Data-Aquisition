fin = open("date.txt", 'r')
dates = fin.readlines()

for i in range(0, len(dates) - 1):
	print 'Now for ' + dates[i][:-1] + '!'
	filename = dates[i][2:-1] + '.csv'
	fp = open(filename, "r")
	filetext = fp.readlines()
	print filetext[len(filetext)]
