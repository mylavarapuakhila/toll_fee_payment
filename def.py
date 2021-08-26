
import mysql.connector
cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tollbooth')
mycursor=cnx.cursor()
s="select * from tolls "
#s="select * from tolls where tolls_from = 'BANGALORE' and tolls_to = 'CHENNAI' or tolls_from = 'CHENNAI' and tolls_to = 'BANGALORE' "


query=(s)
mycursor.execute(query)
for i in mycursor:
	print(i)