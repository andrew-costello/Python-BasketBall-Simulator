# Python Basketball Simulator

A basketball arcade-style simulator built in Python using an SQL database of NBA teams and players.  
The program simulates games minute-by-minute, generating realistic scores based on player statistics, and includes a full tournament/playoff mode.

## Project Overview

This simulator allows users to:

- Simulate games between real NBA teams  
- Generate scores that update every minute of gameplay  
- Track individual player scoring output  
- Simulate realistic variation using averages and standard deviation  
- Create custom teams with your own players and PPG values  
- Run full playoff tournaments with automatic winners  
- Display Game MVP after every match  

Only points per game (PPG) are recorded, keeping the system focused on scoring performance.

## How It Works

1. A database (created separately) stores:
   - NBA teams  
   - Their starting 5 players  
   - Basic player stats = PPG, (standard deviation also calculated in code)

2. When two teams play:
   - The match is simulated minute by minute  
   - Each player’s scoring is generated using their average and deviation  
   - Team scores update throughout the game  
   - At the end, an MVP is selected based on performance  

3. Users can:
   - Simulate real NBA matchups  
   - Build their own fantasy or vintage teams  
   - Run tournament brackets automatically  

## Simulation Logic

- Player scoring is not fixed and changes each game  
- Statistical variation is used to avoid predictable results  
- Every game feels different even with the same teams  
- Designed to mimic arcade-style basketball simulations

## Features

- Minute-by-minute game simulation  
- Player scoring based on real stats  
- Standard deviation for realistic randomness  
- Custom team creation  
- Vintage team support  
- Full tournament and playoff mode  
- Game MVP selection  
- SQL database backend  

## Built With

- Python – core logic and simulation  
- SQL Database – stores teams and player statistics  

## Possible Improvements

- Add assists and rebounds instead of PPG only  
- Graphical interface instead of terminal  
- Season mode with league standings  
- Player fatigue system  
- Export box scores to files  

## About

This project was created as a fun way to simulate basketball games using statistics and randomness, combining sports logic with programming and databases.
