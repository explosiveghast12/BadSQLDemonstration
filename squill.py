# In this file, I will access a DATABASE
# Yo, it works!!!

# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

import mysql.connector
from mysql.connector import errorcode # to handle errors

# It would be smart to use try except to hand errors
# But I'm not being paid to do this


# Okay so, MariaDB actually uses the InnoDB engine
TABULATURE = {}
TABULATURE['data'] = (
    " CREATE TABLE data ( number int(20) NOT NULL) ENGINE=InnoDB"
)

add_data = ("INSERT INTO data"
            "(number)"
            "VALUES (%(whatever)s)")

cnx = mysql.connector.connect(
    database="mysql",
    host="127.0.0.1",
    user="root"
)

curses = cnx.cursor()

print(cnx)

# Check if table already exists, if it doesn't then create the table

try:
    curses.execute(TABULATURE['data'])
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Why are you trying to create a table that already exists?")
    else:
        print(err.msg)
else:
     print("I guess everything is fine since the table was created")

# Add

data = {'whatever': 21}

data_the_second = {'whatever': 201}

curses.execute(add_data, data)

curses.execute(add_data, data_the_second)

# Query

curses.execute('SELECT * FROM data')

for i in curses:
    print(i) #should print 20 or something

# Update

updata = (
     "UPDATE data"
     " SET number = 42"
     " WHERE number = 21"
)

print("UPDATEIFIED!!!")

curses.execute(updata)

# Query again

curses.execute('SELECT * FROM data')

for i in curses:
    print(i) #should print 20 or something

# Delete

lose_your_data = (
     "DROP TABLE data" # Technically this deletes the data...
)

curses.execute(lose_your_data)

cnx.close()