#Module Imports
import mariadb
import sys 

#Connect to MariaDB Platform
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
#Get Cursor 
cur = conn.cursor()

def disp_players(team_name):
    cur.execute(
        "SELECT teams.Team_Name, players.Player_Name, players.Player_Position, players.PPG FROM Player players JOIN Team teams ON players.Player_Team_ID = teams.Team_ID WHERE teams.Team_Name = ?",
        (team_name,)
    )
    
    print("Team Name, Player Name, Position, PPG")
    for (Team_Name, Player_Name, Player_Position, PPG) in cur:
        print(Team_Name, Player_Name, Player_Position, PPG)

    #Print Result-set
    for (Player_Name) in cur: 
        print(f"Player Name: {Player_Name}")
def disp_selected_teams(team1,team2):
    
    #Making 2D Lists
    playersTeam1 = []
    playersTeam2 = []
    
    cur.execute(
        "SELECT teams.Team_Name, players.Player_Name, players.Player_Position, players.PPG FROM Player players JOIN Team teams ON players.Player_Team_ID = teams.Team_ID WHERE teams.Team_Name = ?",
        (team1,)
    )
    print("\nSelected Teams:\n---------------------------------------------------------")
    print("\nTeam 1:\n---------------------------------------------------------")
    print("Team Name, Player Name, Position, PPG")
    for (Team_Name, Player_Name, Player_Position, PPG) in cur:
        playersTeam1.append([Team_Name, Player_Name, Player_Position, PPG])
        print(Team_Name, Player_Name, Player_Position, PPG)
        
    cur.execute(
        "SELECT teams.Team_Name, players.Player_Name, players.Player_Position, players.PPG FROM Player players JOIN Team teams ON players.Player_Team_ID = teams.Team_ID WHERE teams.Team_Name = ?",
        (team2,)
    )
    
    print("\nTeam 2:\n---------------------------------------------------------")
    print("Team Name, Player Name, Position, PPG")
    for (Team_Name, Player_Name, Player_Position, PPG) in cur:
        playersTeam2.append([Team_Name, Player_Name, Player_Position, PPG])
        print(Team_Name, Player_Name, Player_Position, PPG)
    
    return(playersTeam1, playersTeam2)        

def disp_all_teams():
    cur.execute(
        "SELECT Team_Name FROM Team",
    )
    print("\nAll Teams:\n---------------------------------------------------------")
    for (Team_Name,) in cur:
        print(Team_Name)

def create_player(Team_ID):
    Player_Name = input("Enter Players Name: ")
    Player_Position = input("Enter Players Position ('PG'/'SG'/'SF'/'PF'/'C'): ")
    PPG = input("Enter players PPG (e.g '31.4'): ")
    cur.execute(
        "INSERT INTO player (Player_Name, Player_Position, PPG, Player_Team_ID) VALUES (?, ?, ?, ?);", 
        (Player_Name, Player_Position, PPG, Team_ID))

def create_team():
    Team_Name = input("Enter Team Name: ")
    Team_Conference = input("Enter Team Conference ('East' or 'West'): ")
    cur.execute(
    "INSERT INTO team (Team_Name, Team_Conference) VALUES (?,?);",
    (Team_Name, Team_Conference))
    
    cur.execute(
        "SELECT Team_Name, Team_ID, Team_Conference FROM Team WHERE Team_Name = ?",
        (Team_Name,)
    )
    print("\n---------------------------\n")
    print("Team Name, Team ID, Team Conference")
    for (Team_Name, Team_ID, Team_Conference) in cur:
        print(Team_Name, Team_Conference)
    print("\n---------------------------\n")
    print("Team added, now add some players.\n")
    
    for i in range(1,6):
        print("Creaing player "+str(i)+" of 5")
        create_player(Team_ID)
        
    cur.execute(
        "SELECT teams.Team_Name, players.Player_Name, players.Player_Position, players.PPG FROM Player players JOIN Team teams ON players.Player_Team_ID = teams.Team_ID WHERE teams.Team_Name = ?",
        (Team_Name,)
    )
    print("\nCreated Team:\n---------------------------------------------------------")
    print("Team Name, Player Name, Position, PPG")
    for (Team_Name, Player_Name, Player_Position, PPG) in cur:
        print(Team_Name, Player_Name, Player_Position, PPG)
    conn.commit()
    
#Disable Auto-Commit
conn.autocommit = False
conn.commit()
print(f"Last Inserted ID: {cur.lastrowid}")
