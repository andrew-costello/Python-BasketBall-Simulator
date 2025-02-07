import math
import random
import time

random.seed(time.time())

def calc_Points(TwoD1, TwoD2):
    players1PointsCalc = [0,0,0,0,0]
    players2PointsCalc = [0,0,0,0,0]
    modulus1 = 0
    modulus2 = 0
    players1Points = [0,0,0,0,0] 
    players2Points = [0,0,0,0,0] 
    std_dev = 1

    for i in range(48):
        for j, (row1, row2) in enumerate(zip(TwoD1, TwoD2)):
            # Process TwoD1
            avg_ppg_1 = row1[4]  # Assume row[3] is the average points per game
            ppgD48_1 = avg_ppg_1 / 48  # Expected contribution per iteration
            simulated_points_1 = random.gauss(ppgD48_1, std_dev)
            players1PointsCalc[j] += max(0, simulated_points_1)
            modulus1 = players1PointsCalc[j] % 2
            if 0 <= modulus1 < 1:
                players1Points[j] = math.floor(players1PointsCalc[j])

            # Process TwoD2
            avg_ppg_2 = row2[4]  # Assume row[3] is the average points per game
            ppgD48_2 = avg_ppg_2 / 48  # Expected contribution per iteration
            simulated_points_2 = random.gauss(ppgD48_2, std_dev)
            players2PointsCalc[j] += max(0, simulated_points_2)
            modulus2 = players2PointsCalc[j] % 2
            if 0 <= modulus2 < 1:
                players2Points[j] = math.floor(players2PointsCalc[j])

            # Print with a gap between TwoD1 and TwoD2
            print(f"{row1[2]:<20} {players1Points[j]:<5}  |  {row2[2]:<20} {players2Points[j]:<5}")
        print("------------------------")
        print(row1[0]+": "+str(sum(players1Points))+" "+row2[0]+": "+str(sum(players2Points)))

        # Wait for 1 second before the next iteration
        time.sleep(2)
                
    