import mysql.connector as c
con=c.connect(host="localhost",
              user="root",
              passwd="mysql",
              database="movie")
cursor=con.cursor()