# chatGPT generated! 
from termcolor import colored
import random
import os
import sys

# ASCII characters for the different dungeon elements
wall = "#"
floor = "."
player = "@"

# Dungeon dimensions
width = 80
height = 25

# Initialize the dungeon with empty spaces
dungeon = [[floor for x in range(width)] for y in range(height)]

# Add walls around the perimeter of the dungeon
for x in range(width):
    dungeon[0][x] = wall
    dungeon[height-1][x] = wall
for y in range(height):
    dungeon[y][0] = wall
    dungeon[y][width-1] = wall

# Randomly place walls in the interior of the dungeon
for y in range(1, height-1):
    for x in range(1, width-1):
        if random.random() < 0.3:
            dungeon[y][x] = wall

# Initial position of the player
player_x = width//2
player_y = height//2
dungeon[player_y][player_x] = player

# Game loop
while True:
    os.system('clear')  # Clear the screen
    for y in range(height):
        for x in range(width):
            if dungeon[y][x] == wall:
                print(colored(dungeon[y][x], 'grey'), end="")
            elif dungeon[y][x] == player:
                print(colored(dungeon[y][x], 'green'), end="")
            else:
                print(colored(dungeon[y][x], 'white'), end="")
        print()

    # Get user input
    key = sys.stdin.read(1)

    # Update player position based on user input
    if key == 'w':
        if dungeon[player_y-1][player_x] != wall:
            dungeon[player_y][player_x] = floor
            player_y -= 1
            dungeon[player_y][player_x] = player
    elif key == 's':
        if dungeon[player_y+1][player_x] != wall:
            dungeon[player_y][player_x] = floor
            player_y += 1
            dungeon[player_y][player_x] = player
    elif key == 'a':
        if dungeon[player_y][player_x-1] != wall:
            dungeon[player_y][player_x] = floor
            player_x -= 1
            dungeon[player_y][player_x] = player
    elif key == 'd':
        if dungeon[player_y][player_x+1] != wall:
            dungeon[player_y][player_x] = floor
            player_x += 1
            dungeon[player_y][player_x] = player
    elif key == 'q':
        break
