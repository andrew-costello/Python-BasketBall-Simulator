'''File to connect with the Basketball database.'''
import sys
import mariadb

positions = ["PG", "SG", "SF", "PF", "C"]
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="root100",
        host="127.0.0.1",
        port=3306,
        database="BasketballDataB",
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
# Get Cursor
cur = conn.cursor()


def disp_players(team_name):
    '''Function to display players on a team'''
    cur.execute(
        "SELECT teams.Team_Name, players.Player_Name, players.Player_Position, players.PPG FROM Player players JOIN Team teams ON players.Player_Team_ID = teams.Team_ID WHERE teams.Team_Name = ?",
        (team_name,),
    )

    print("Team Name, Player Name, Position, PPG")
    for team_name, player_name, player_position, ppg in cur:
        print(team_name, player_name, player_position, ppg)

    # Print Result-set
    for player_name in cur:
        print(f"Player Name: {player_name}")


def disp_selected_teams(team1, team2):
    '''Function to display the teams that are selected to play a game.'''
    # Making 2D Lists
    players_team1 = []
    players_team2 = []

    try:
        # Query for the first team
        cur.execute(
            "SELECT teams.Team_Name, players.Player_Name, players.Player_Position, players.PPG "
            "FROM Player players JOIN Team teams ON players.Player_Team_ID = teams.Team_ID "
            "WHERE teams.Team_Name = ?",
            (team1,),
        )
        for team_name, player_name, player_position, ppg in cur:
            players_team1.append([team_name, player_name, player_position, ppg])

        if not players_team1:
            print(f"No players found for team '{team1}'. Please check the team name.")

        # Query for the second team
        cur.execute(
            "SELECT teams.Team_Name, players.Player_Name, players.Player_Position, players.PPG "
            "FROM Player players JOIN Team teams ON players.Player_Team_ID = teams.Team_ID "
            "WHERE teams.Team_Name = ?",
            (team2,),
        )
        for team_name, player_name, player_position, ppg in cur:
            players_team2.append([team_name, player_name, player_position, ppg])

        if not players_team2:
            print(f"No players found for team '{team2}'. Please check the team name.")

    except mariadb.Error as e:
        print(f"An error occurred while accessing the database: {e}")

    # Display selected teams
    print(
        "\nSelected Teams:\n---------------------------------------------------------"
    )
    print("\nTeam 1:\n---------------------------------------------------------")
    print("Team Name, Player Name, Position, PPG")
    for player in players_team1:
        print(player)

    print("\nTeam 2:\n---------------------------------------------------------")
    print("Team Name, Player Name, Position, PPG")
    for player in players_team2:
        print(player)

    return players_team1, players_team2


def disp_all_teams():
    '''Function to display all teams'''
    cur.execute(
        "SELECT Team_Name FROM Team",
    )
    print("\nAll Teams:\n---------------------------------------------------------")
    for (team_name,) in cur:
        print(team_name)


def create_player(team_id, player_position):
    '''Function to create a player.'''
    player_name = input("Enter Players Name: ")
    ppg = input("Enter players PPG (e.g '31.4'): ")
    cur.execute(
        "INSERT INTO player (Player_Name, Player_Position, PPG, Player_Team_ID) VALUES (?, ?, ?, ?);",
        (player_name, player_position, ppg, team_id),
    )


def create_team():
    '''Function to create a team.'''
    team_name = input("Enter Team Name: ")
    team_conference = input("Enter Team Conference ('East' or 'West'): ")
    cur.execute(
        "INSERT INTO team (Team_Name, Team_Conference) VALUES (?,?);",
        (team_name, team_conference),
    )

    cur.execute(
        "SELECT Team_Name, Team_ID, Team_Conference FROM Team WHERE Team_Name = ?",
        (team_name,),
    )
    print("\n---------------------------\n")
    print("Team Name, Team Conference")
    for team_name, Team_ID, team_conference in cur:
        print(team_name, team_conference)
    print("\n---------------------------\n")
    print("Team added, now add some players.\n")

    for i in range(5):
        print("\n\nCreaing player " + str(i + 1) + " of 5")
        print("\nEnter the details of the " + positions[i] + ".\n")
        create_player(Team_ID, positions[i])

    cur.execute(
        "SELECT teams.Team_Name, players.Player_Name, players.Player_Position, players.PPG FROM Player players JOIN Team teams ON players.Player_Team_ID = teams.Team_ID WHERE teams.Team_Name = ?",
        (team_name,),
    )
    print("\nCreated Team:\n---------------------------------------------------------")
    print("Team Name, Player Name, Position, PPG")
    for team_name, Player_Name, Player_Position, PPG in cur:
        print(team_name, Player_Name, Player_Position, PPG)
    conn.commit()


def disp_selected_team(team1):
    '''Function to display a selected team'''
    # Making 2D Lists
    players_team1 = []

    cur.execute(
        "SELECT teams.Team_Name, players.Player_Name, players.Player_Position, players.PPG FROM Player players JOIN Team teams ON players.Player_Team_ID = teams.Team_ID WHERE teams.Team_Name = ?",
        (team1,),
    )
    print(
        "\nSelected Teams:\n---------------------------------------------------------"
    )
    print("\nTeam 1:\n---------------------------------------------------------")
    print("Team Name, Player Name, Position, PPG")
    for team_name, player_name, player_position, ppg in cur:
        players_team1.append([team_name, player_name, player_position, ppg])
        print(team_name, player_name, player_position, ppg)

    return players_team1


# Disable Auto-Commit
conn.autocommit = False
conn.commit()
print(f"Last Inserted ID: {cur.lastrowid}")
