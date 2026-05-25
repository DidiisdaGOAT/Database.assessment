import sqlite3

DATABASE = "Baskatball_stats"

#Defining the functions

db = sqlite3.connect("Basketball_stats")
cursor = db.cursor()
sql = "SELECT * FROM team"
cursor.execute(sql)
results = cursor.fetchall()
print("Last Name               First Name    Jersey Number   PPG    Total Points")
for player in results:
    print(f"{player[1]:<24}{player[2]:<15}#{player[3]:<14}{player[4]:<8}{player[5]:<14}{player[6]:<6}{player[7]:<6}{player[8]}")
db.close()    