from contextlib import closing
import MySQLdb
import csv

mydb = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'imdb')
cursor = mydb.cursor()

with open('person_names.txt', 'r') as source:
	rdr = csv.reader(source, delimiter = '\n', quotechar = ',')
	count = 0
	for row in rdr:
		name = row[0]
		cursor.execute('UPDATE user SET name=%s WHERE id=%s', (name, count))
		count = count + 1

# close the connection to the database.
mydb.commit()
cursor.close()
print "Done"