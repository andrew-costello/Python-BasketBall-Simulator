import basketballDB
import game


team1 = ""
team2 = ""
playersTeam1 = []
playersTeam2 = []

def menu():
    while True:
        option = int(input("\n\n----------------------------------------------\nWelcome to my Python Arcade Basketball Game!\n----------------------------------------------\n\nWhat do you wish to do?\nPlay a Game?: Press '1'\nList all teams?: Press '2'\nList all players in 'x' team?: Press '3'\nCreate a team?: Press '4'\nExit: Press '5'\n\nEnter option: "))
        
        if option == 5:
            print("\nExiting...")
            break  #Exit the loop and the program
        
        options(option)

def options(option):
    if option == 1:
        
        #Function for picking teams
        def pick_teams():
            basketballDB.disp_all_teams()
            teamX = input("Enter the name of the first team name: ")
            teamY = input("Enter the name of the second team name: ")
            return(teamX,teamY)

        team1,team2 = pick_teams()
        playersTeam1,playersTeam2 = basketballDB.disp_selected_teams(team1,team2)
        
        print (playersTeam1)
        print (playersTeam2)

        #Run the function to play the game
        game.calc_Points(playersTeam1,playersTeam2)
        
    elif option == 2: 
        #Run the function to display all of the teams available
        basketballDB.disp_all_teams()
        
    elif option == 3:
        team = input("\nWhat is the name of the team?: ")
        #Run the function to display all players in a team.
        basketballDB.disp_players(team)
        

    elif option == 4:
        #Run the function to create a team.
        basketballDB.create_team()
        
menu()
