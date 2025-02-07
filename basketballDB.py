# Module Imports
import mariadb
import sys 

first_name = "Ben"
# Connect to MariaDB Platform
try: conn = mariadb.connect( 
    user="root", 
    password="root100", 
    host="127.0.0.1", 
    port=3306, 
    database="BasketballDataB" 
) 
except mariadb.Error as e: 
    print(f"Error connecting to MariaDB Platform: {e}") 
    sys.exit(1) 
# Get Cursor 
cur = conn.cursor()

def disp_player():
    cur.execute(
        "SELECT First_Name,Last_Name FROM player WHERE First_Name=?", 
        (first_name,)
    )

    # Print Result-set
    for (First_Name, Last_Name) in cur: 
        print(f"First Name: {First_Name}, Last Name: {Last_Name}")

def disp_selected_teams(team1,team2):
    
    #Making 2D Lists
    playersTeam1 = []
    playersTeam2 = []
    
    cur.execute(
        "SELECT teams.Team_Name, players.First_Name, players.Last_Name, players.Player_Position, players.PPG, players.RPG, players.APG FROM Player players JOIN Team teams ON players.Player_Team_ID = teams.Team_ID WHERE teams.Team_Name = ?",
        (team1,)
    )
    print(f"\nSelected Teams:\n---------------------------------------------------------")
    print(f"\nTeam 1:\n---------------------------------------------------------")
    print(f"Team Name, Player Name, Position, PPG, RPG, APG")
    for (Team_Name, First_Name, Last_Name, Player_Position, PPG, RPG, APG) in cur:
        playersTeam1.append([Team_Name,First_Name, Last_Name, Player_Position, PPG, RPG, APG])
        print(Team_Name, First_Name, Last_Name, Player_Position, PPG, RPG, APG)
        
    cur.execute(
        "SELECT teams.Team_Name, players.First_Name, players.Last_Name, players.Player_Position, players.PPG, players.RPG, players.APG FROM Player players JOIN Team teams ON players.Player_Team_ID = teams.Team_ID WHERE teams.Team_Name = ?",
        (team2,)
    )
    
    print(f"\nTeam 2:\n---------------------------------------------------------")
    print(f"Team Name, Player Name, Position, PPG, RPG, APG")
    for (Team_Name, First_Name, Last_Name, Player_Position, PPG, RPG, APG) in cur:
        playersTeam2.append([Team_Name,First_Name, Last_Name, Player_Position, PPG, RPG, APG])
        print(Team_Name, First_Name, Last_Name, Player_Position, PPG, RPG, APG)
    
    return(playersTeam1, playersTeam2)        

def disp_all_teams():
    cur.execute(
        "SELECT Team_Name FROM Team",
    )
    print(f"\nAll Teams:\n---------------------------------------------------------")
    for (Team_Name) in cur:
        print(Team_Name)

def create_player(First_Name, Last_Name, Player_Position, PPG, RPG, APG, Player_Team_ID):
    cur.execute(
        "INSERT INTO player (First_Name, Last_Name, Player_Position, PPG, RPG, APG, Player_Team_ID) VALUES (?, ?, ?, ?, ?, ?, ?);", 
        (First_Name, Last_Name, Player_Position, PPG, RPG, APG, Player_Team_ID))

# Disable Auto-Commit
conn.autocommit = False
conn.commit()
print(f"Last Inserted ID: {cur.lastrowid}")