import sqlite3

DATABASE = "Baskatball_stats"
db = sqlite3.connect("Basketball_stats")
cursor = db.cursor()



#Defining the functions
 
def print_all_players():
    sql = "SELECT * FROM team"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Last Name               First Name    Jersey Number  PPG    Total  High  Fouls Games Played")
    #Making a for loop
    for player in results:
        print(f"{player[1]:<24}{player[2]:<14}#{player[3]:<14}{player[4]:<8}{player[5]:<6}{player[6]:<6}{player[7]:<6}{player[8]}")
   


def print_all_players_by_last_name():
    sql = "SELECT * FROM team ORDER BY last_name"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Making a for loop
    print("Last Name               First Name    Jersey Number  PPG    Total  High  Fouls Games Played")
    for player in results:
        print(f"{player[1]:<24}{player[2]:<14}#{player[3]:<14}{player[4]:<8}{player[5]:<6}{player[6]:<6}{player[7]:<6}{player[8]}")



def print_all_players_by_first_name():
    sql = "SELECT * FROM team ORDER BY first_name"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Making a for loop
    print("Last Name               First Name    Jersey Number  PPG    Total  High  Fouls Games Played")
    for player in results:
        print(f"{player[1]:<24}{player[2]:<14}#{player[3]:<14}{player[4]:<8}{player[5]:<6}{player[6]:<6}{player[7]:<6}{player[8]}")

 

def print_all_players_by_jersey_number():
    sql = "SELECT * FROM team ORDER BY jersey_number"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Making a for loop
    print("Last Name               First Name    Jersey Number  PPG    Total  High  Fouls Games Played")
    for player in results:
        print(f"{player[1]:<24}{player[2]:<14}#{player[3]:<14}{player[4]:<8}{player[5]:<6}{player[6]:<6}{player[7]:<6}{player[8]}")



def print_all_players_by_ppg():
    sql = "SELECT * FROM team ORDER BY ppg DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Making a for loop
    print("Last Name               First Name    Jersey Number  PPG    Total  High  Fouls Games Played")
    for player in results:
        print(f"{player[1]:<24}{player[2]:<14}#{player[3]:<14}{player[4]:<8}{player[5]:<6}{player[6]:<6}{player[7]:<6}{player[8]}")


def print_all_players_by_total_points():
    sql = "SELECT * FROM team ORDER BY total_points DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Making a for loop
    print("Last Name               First Name    Jersey Number  PPG    Total  High  Fouls Games Played")
    for player in results:
        print(f"{player[1]:<24}{player[2]:<14}#{player[3]:<14}{player[4]:<8}{player[5]:<6}{player[6]:<6}{player[7]:<6}{player[8]}")       


def print_all_players_by_season_high():
    sql = "SELECT * FROM team ORDER BY season_high DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Making a for loop
    print("Last Name               First Name    Jersey Number  PPG    Total  High  Fouls Games Played")
    for player in results:
        print(f"{player[1]:<24}{player[2]:<14}#{player[3]:<14}{player[4]:<8}{player[5]:<6}{player[6]:<6}{player[7]:<6}{player[8]}")


def print_all_players_by_fouls():
    sql = "SELECT * FROM team ORDER BY fouls DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Making a for loop
    print("Last Name               First Name    Jersey Number  PPG    Total  High  Fouls Games Played")
    for player in results:
        print(f"{player[1]:<24}{player[2]:<14}#{player[3]:<14}{player[4]:<8}{player[5]:<6}{player[6]:<6}{player[7]:<6}{player[8]}")


def print_all_players_by_games_played():
    sql = "SELECT * FROM team ORDER BY games_played DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Making a for loop
    print("Last Name               First Name    Jersey Number  PPG    Total  High  Fouls Games Played")
    for player in results:
        print(f"{player[1]:<24}{player[2]:<14}#{player[3]:<14}{player[4]:<8}{player[5]:<6}{player[6]:<6}{player[7]:<6}{player[8]}")

        
#Main code
print_all_players_by_games_played()
db.close()