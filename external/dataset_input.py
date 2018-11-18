import psycopg2
import csv

conn_string = "host='localhost' dbname='postgres' user='postgres' password='server'"

database = psycopg2.connect (conn_string)

cursor = database.cursor()

#cursor.execute(Create Table location(LON float, LAT float);)

print("Table created successfully")

with open('hitrim.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:
		cursor.execute("INSERT INTO location VALUES (%s, %s)",row)

print("Data inserted successfully")
cursor.close()
database.commit()
database.close()
