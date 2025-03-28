'''File to simulate a basketball game.'''
import math
import random
import time

random.seed(time.time())

def calc_points(two_d1, two_d2, time_given):
    '''Function for calculating points'''
    players1_points_calc = [0, 0, 0, 0, 0]
    players2_points_calc = [0, 0, 0, 0, 0]
    players1_points = [0, 0, 0, 0, 0]
    players2_points = [0, 0, 0, 0, 0]
    std_dev = 0.6
    is_overtime = False
    quarter_number = 0

    while True:
        for i in range(time_given):
            for j, (row1, row2) in enumerate(zip(two_d1, two_d2)):
                #Processing the first Teams players PPG
                avg_ppg_1 = row1[3]
                ppgD48_1 = avg_ppg_1 / 48
                simulated_points_1 = random.gauss(ppgD48_1, std_dev)
                players1_points_calc[j] += max(0, simulated_points_1)
                modulus1 = players1_points_calc[j] % 2
                if 0 <= modulus1 < 1:
                    players1_points[j] = math.floor(players1_points_calc[j])
                #Processing the second Teams players PPG
                avg_ppg_2 = row2[3]
                ppgD48_2 = avg_ppg_2 / 48
                simulated_points_2 = random.gauss(ppgD48_2, std_dev)
                players2_points_calc[j] += max(0, simulated_points_2)
                modulus2 = players2_points_calc[j] % 2
                if 0 <= modulus2 < 1:
                    players2_points[j] = math.floor(players2_points_calc[j])

                #Printing scores of each player with a gap between teams.
                print(f"{row1[1]:<30} {row1[2]:<10} {players1_points[j]:<5}  |  {row2[1]:<30} {row2[2]:<10} {players2_points[j]:<5}")
            print("------------------------")
            #Printing the total scores
            print(row1[0] + ": " + str(sum(players1_points)) + " " + row2[0] + ": " + str(sum(players2_points)))

            #Calculating the time left in the game
            if not is_overtime:
                if i % 12 == 0:
                    quarter_number = i // 12 + 1
                    minutes = 12
                minutes -= 1
                print("Q" + str(quarter_number) + " " + str(minutes) + ":00")
            else:
                if i == 0:
                    minutes = 5
                minutes -= 1
                print("OT " + str(minutes) + ":00")

            #Wait for 2 seconds before continuing to the next minute
            time.sleep(2                                               )

        #Check if scores are tied and handle overtime
        if sum(players1_points) == sum(players2_points):
            if not is_overtime:
                print("Scores tied at end of regulation. Going into overtime!")
                time_given = 5
                is_overtime = True
            else:
                print("Scores tied after overtime. Further overtime or declare draw (not implemented).")
                break
        else:
            break
    highest_player_points = max(players1_points)

    if sum(players1_points) > sum(players2_points):
        highest_player_points = max(players1_points)
        player_index = players1_points.index(highest_player_points)
        player_of_the_game = two_d1[player_index][1]
        return (1, 0, player_of_the_game)
    elif sum(players2_points) > sum(players1_points):
        highest_player_points = max(players2_points)
        player_index = players2_points.index(highest_player_points)
        player_of_the_game = two_d2[player_index][1]
        return (0, 1, player_of_the_game)
