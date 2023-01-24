# from chatGPT
from termcolor import colored
from prettytable import PrettyTable
import random
import os
import sys

player_hp = 10
player_attack = 5
player_defense = 5


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
    
# Show the character sheet
    elif key == 'c':
        table = PrettyTable()
        table.field_names = ["Stat", "Value"]
        table.add_row(["HP", colored(str(player_hp), 'red')])
        table.add_row(["Attack", colored(str(player_attack), 'green')])
        table.add_row(["Defense", colored(str(player_defense), 'yellow')])
        print(table)
        input("Press enter to continue...")
    elif key == 'q':
        break
