import basketballDB
import game


team1 = ""
team2 = ""
playersTeam1 = []
playersTeam2 = []
def pick_teams(teamX,teamY):
    basketballDB.disp_all_teams()
    teamX = input("Enter the name of the first team: ")
    teamY = input("Enter the name of the second team: ")
    return(teamX,teamY)

team1,team2 = pick_teams(team1,team2)
playersTeam1,playersTeam2 = basketballDB.disp_selected_teams(team1,team2)

game.calc_Points(playersTeam1,playersTeam2)