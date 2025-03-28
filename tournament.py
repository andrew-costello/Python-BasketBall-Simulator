'''File for running a tournement.'''
import time
import basketball_db
import game

def intro():
    '''Function to introduce the tournements, and list the teams in the tournament.'''
    east_teams = []
    west_teams = []

    east_team_names = []
    west_team_names = []
    
    results_east = []
    results_west = []
    
    print("So this is how it works......")
    time.sleep(2)
    print("You must select 8 teams for each side of the tournament bracket (Just like East and West playoffs in the NBA.).")
    time.sleep(2)
    print("Here are the teams that you can choose from: \n")
    time.sleep(1)
    basketball_db.disp_all_teams()
    time.sleep(1)
    
    for i in range(8):
        print("EAST\n")
        team_east = input("\nWhat is the name team "+str(i)+"?: ")
        east_team_names.append(team_east)
    
    for i in range(8):
        print("WEST\n")
        team_west = input("\nWhat is the name team "+str(i)+"?: ")
        west_team_names.append(team_west)
        
    print("East Team Names:\n")
    print(east_team_names)
    
    print("West Team Names:\n")
    print(west_team_names)
    
    for team in east_team_names:
        team_east_final = basketball_db.disp_selected_team(team)
        east_teams.append(team_east_final)
        
    print(east_teams)
        
    for team in west_team_names:
        team_west_final = basketball_db.disp_selected_team(team)
        west_teams.append(team_west_final)
        
    print(east_teams)
    print(west_teams)
    print("\n------------------------------")    
    print("ROUND 1!!!!!")
    print("\n------------------------------")  
     
    results_east, results_west = sim_games(east_teams, west_teams)
    
    east_teams = [team for binary, team in zip(results_east, east_teams) if binary == 1]
    west_teams = [team for binary, team in zip(results_west, west_teams) if binary == 1]
    
    east_teams = east_teams[:4]
    west_teams = west_teams[:4]
    
    print("\n------------------------------")    
    print("Conference Semi-Finals!!!!!")
    print("\n------------------------------") 
    
    results_east, results_west = sim_games(east_teams, west_teams)
    
    east_teams = [team for binary, team in zip(results_east, east_teams) if binary == 1]
    west_teams = [team for binary, team in zip(results_west, west_teams) if binary == 1]
    
    east_teams = east_teams[:2]
    west_teams = west_teams[:2]
    
    print("\n------------------------------")    
    print("Conference Finals!!!!!")
    print("\n------------------------------") 
    
    results_east, results_west = sim_games(east_teams, west_teams)
    
    east_teams = [team for binary, team in zip(results_east, east_teams) if binary == 1]
    west_teams = [team for binary, team in zip(results_west, west_teams) if binary == 1]
    
    east_teams = east_teams[:1]
    west_teams = west_teams[:1]
    
    print("\n------------------------------")    
    print("Basketball Finals!!!!!")
    print("\n------------------------------") 
    
    
    result1, result2, finals_mvp = game.calc_points(east_teams[0], west_teams[0], 48)
    
    east_teams = [team for binary, team in zip(results_east, east_teams) if binary == 1]
    west_teams = [team for binary, team in zip(results_west, west_teams) if binary == 1]
    print("------------------------")
    
    if result1 == 1:
        return (result1,finals_mvp)
    else:
        return (result2,finals_mvp)
    
    #East_Teams,West_Teams = basketballDB.start_tournament()  
def sim_games(east_teams, west_teams):
    '''Function to run each game'''
    results_east = []
    results_west = []
    
    for i in range (0, len(east_teams), 2):
        team1 = east_teams[i]
        team2 = east_teams[i + 1]
        result1, result2, potg = game.calc_points(team1, team2, 48)
        results_east.append(result1)
        results_east.append(result2)
        print(f"East Game: {team1[0]} vs {team2[0]}, Results: {result1}, {result2}, POTG: {potg}")
            
    for i in range (0, len(west_teams), 2):
        team1 = west_teams[i]
        team2 = west_teams[i + 1]
        result1, result2, potg = game.calc_points(team1, team2, 48)
        results_west.append(result1)
        results_west.append(result2)
        print(f"West Game: {team1[0]} vs {team2[0]}, Results: {result1}, {result2}, POTG: {potg}")
    
    return (results_east, results_west)
