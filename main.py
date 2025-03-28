"""Main menu page for basketball game."""

import basketball_db
import game
import tournament


TEAM1 = ""
TEAM2 = ""
players_team1 = []
players_team2 = []

east_teams = []
west_teams = []


def menu():
    """Function to get option for which action you want to do."""
    while True:
        option = int(input("\n\n----------------------------------------------\nWelcome to my Python Arcade Basketball Game!\n----------------------------------------------\n\nWhat do you wish to do?\nPlay a Game?: Press '1'\nPlay a Tournement?: Press '2'\nList all teams?: Press '3'\nList all players in 'x' team?: Press '4'\nCreate a team?: Press '5'\nExit: Press '6'\n\nEnter option: "))
        if option == 6:
            print("\nExiting...")
            break  # Exit the loop and the program
        options(option)


def options(option):
    """Function to run each option on the menu."""
    if option == 1:
        basketball_db.disp_all_teams()

        while True:
            team1 = input("Enter the name of the first team: ")
            team2 = input("Enter the name of the second team: ")
            players_team1, players_team2 = basketball_db.disp_selected_teams(
                team1, team2
            )

            # Check if both teams have players; if not, print an error and repeat the input process
            if players_team1 and players_team2:
                break  # Exit the loop if valid teams are entered
            else:
                print(
                    "One or both team names are incorrect. Please enter valid team names.\n"
                )

        # Run the function to play the game
        result1, result2, mvp = game.calc_points(players_team1, players_team2, 48)
        print(mvp)

    elif option == 2:
        winning_team, finals_mvp = tournament.intro()
        print("\n")
        print("Finals MVP is: " + finals_mvp)
        print("-----------------------------")
    elif option == 3:
        # Run the function to display all of the teams available
        basketball_db.disp_all_teams()
    elif option == 4:
        team = input("\nWhat is the name of the team?: \n\n")
        # Run the function to display all players in a team.
        basketball_db.disp_players(team)
    elif option == 5:
        # Run the function to create a team.
        basketball_db.create_team()


menu()
