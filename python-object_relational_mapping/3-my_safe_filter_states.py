#import MySQLdb & sys
import MySQLdb
from sys import argv

#connecting to mysqldb
db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

#getting a cursor 
cur = db.cursor()

#executing our script that is safe from sql injections 
cur.execute("SELECT * from states WHERE name LIKE %s ORDER BY states.id",(argv[4]))

#printing result
myresult = cur.fetchall()
for state in myresult:
  print(state)


# Closing all cursors and databases
cur.close()
db.close()