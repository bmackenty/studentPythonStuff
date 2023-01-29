# this file was written by a student for a project
import os
import wordle_list
import random

os.system("clear")

first_guess_one=input("enter your first letter: ")
first_results_one=input("enter your results (c - correct y - yellow, g - gray): ")

first_one_list =[]
if first_results_one == "g":
    for j in wordle_list.all_words:
        if first_guess_one not in j:
            first_one_list.append(j)
for i in wordle_list.all_words:
    if first_guess_one in i: 
        if first_results_one == "c":
            if i[0] == first_guess_one:
                first_one_list.append(i)
        if first_results_one == "y":
            if i[0] != first_guess_one:
                if i[1] == first_guess_one or i[2] == first_guess_one or i[3] == first_guess_one or i[4] == first_guess_one:
                    first_one_list.append(i)

print(first_one_list)

second_guess_one=input("enter your second letter: ")
second_results_one=input("enter your results (c - correct y - yellow, g - gray): ")

second_one_list =[] 
if second_results_one == "g": 
    for j in first_one_list: 
        if second_guess_one not in j:
            second_one_list.append(j) 
for i in first_one_list:
    if second_guess_one in i: 
        if second_results_one == "c":
            if i[1] == second_guess_one:
                second_one_list.append(i)
        if second_results_one == "y":
            if i[1] != second_guess_one:
                if i[0] == second_guess_one or i[2] == second_guess_one or i[3] == second_guess_one or i[4] == second_guess_one:
                    second_one_list.append(i)
 
print(second_one_list)


third_guess_one=input("enter your third letter: ")
third_results_one=input("enter your results (c - correct y - yellow, g - gray): ")

third_one_list =[]
if third_results_one == "g": 
    for j in second_one_list: 
        if third_guess_one not in j:
            third_one_list.append(j) 
for i in second_one_list:
    if third_guess_one in i: 
        if third_results_one == "c":
            if i[2] == third_guess_one:
                third_one_list.append(i)
        if third_results_one == "y":
            if i[2] != third_guess_one:
                if i[0] == third_guess_one or i[1] == third_guess_one or i[3] == third_guess_one or i[4] == third_guess_one:
                    third_one_list.append(i)
print(third_one_list)

fourth_guess_one=input("enter your fourth letter: ")
fourth_results_one=input("enter your results (c - correct y - yellow, g - gray): ")

fourth_one_list = []
if fourth_results_one == "g": 
    for j in third_one_list: 
        if fourth_guess_one not in j:
            fourth_one_list.append(j) 
for i in third_one_list:
    if fourth_guess_one in i: 
        if fourth_results_one == "c":
            if i[3] == fourth_guess_one:
                fourth_one_list.append(i)
        if fourth_results_one == "y":
            if i[3] != third_guess_one:
                if i[0] == fourth_guess_one or i[1] == fourth_guess_one or i[2] == fourth_guess_one or i[4] == fourth_guess_one:
                    fourth_one_list.append(i)

print(fourth_one_list)

fifth_guess_one=input("enter your fifth letter: ")
fifth_results_one=input("enter your results (c - correct y - yellow, g - gray): ")

fifth_one_list = []
if fifth_results_one == "g": 
    for j in fourth_one_list: 
        if fifth_guess_one not in j:
            fifth_one_list.append(j) 
for i in fourth_one_list:
    if fifth_guess_one in i: 
        if fifth_results_one == "c":
            if i[4] == fifth_guess_one:
                fifth_one_list.append(i)
        if fifth_results_one == "y":
            if i[4] != fifth_guess_one:
                if i[0] == fifth_guess_one or i[1] == fifth_guess_one or i[2] == fifth_guess_one or i[4] == fifth_guess_one:
                    fifth_one_list.append(i)
print(fifth_one_list)

if len(fifth_one_list) == 1:
    print("You have solved the puzzle!")

# ---------------------------------------------------------- 2 --------------------------------------------------------

first_guess_two=input("enter your first letter of the second word: ")
first_results_two=input("enter your results (c - correct y - yellow, g - gray): ")

first_two_list =[]
if first_results_two == "g": 
    for j in fifth_one_list: 
        if first_guess_two not in j:
            first_two_list.append(j) 
for i in fifth_one_list:
    if first_guess_two in i: 
        if first_results_two == "c":
            if i[0] == first_guess_two:
                first_two_list.append(i)
        if first_results_two == "y":
            if i[0] != first_guess_two:
                if i[1] == first_guess_two or i[2] == first_guess_two or i[3] == first_guess_two or i[4] == first_guess_two:
                    first_two_list.append(i)

print(first_two_list) 

second_guess_two=input("enter your second letter: ")
second_results_two=input("enter your results (c - correct y - yellow, g - gray): ")

second_two_list =[]
if second_results_two == "g": 
    for j in first_two_list: 
        if second_guess_two not in j:
            second_two_list.append(j) 
for i in first_two_list:
    if second_guess_two in i: 
        if second_results_two == "c":
            if i[1] == second_guess_two:
                second_two_list.append(i)
        if second_results_two == "y":
            if i[1] != second_guess_two:
                if i[0] == second_guess_two or i[2] == second_guess_two or i[3] == second_guess_two or i[4] == second_guess_two:
                    second_two_list.append(i)

print(second_two_list)


third_guess_two=input("enter your third letter: ")
third_results_two=input("enter your results (c - correct y - yellow, g - gray): ")

third_two_list =[]
if third_results_two == "g": 
    for j in second_two_list: 
        if third_guess_two not in j:
            third_two_list.append(j) 
for i in second_two_list:
    if third_guess_two in i: 
        if third_results_two == "c":
            if i[2] == third_guess_two:
                third_two_list.append(i)
        if third_results_two == "y":
            if i[2] != third_guess_two:
                if i[0] == third_guess_two or i[1] == third_guess_two or i[3] == third_guess_two or i[4] == third_guess_two:
                    third_two_list.append(i)
print(third_two_list)

fourth_guess_two=input("enter your fourth letter: ")
fourth_results_two=input("enter your results (c - correct y - yellow, g - gray): ")

fourth_two_list = []
if fourth_results_two == "g": 
    for j in third_two_list: 
        if fourth_guess_two not in j:
            fourth_two_list.append(j) 
for i in third_two_list:
    if fourth_guess_two in i: 
        if fourth_results_two == "c":
            if i[3] == fourth_guess_two:
                fourth_two_list.append(i)
        if fourth_results_two == "y":
            if i[3] != third_guess_two:
                if i[0] == fourth_guess_two or i[1] == fourth_guess_two or i[2] == fourth_guess_two or i[4] == fourth_guess_two:
                    fourth_two_list.append(i)

print(fourth_two_list)

fifth_guess_two=input("enter your fifth letter: ")
fifth_results_two=input("enter your results (c - correct y - yellow, g - gray): ")

fifth_two_list = []
if fifth_results_two == "g": 
    for j in fourth_two_list: 
        if fifth_guess_two not in j:
            fifth_two_list.append(j) 
for i in fourth_two_list:
    if fifth_guess_two in i: 
        if fifth_results_two == "c":
            if i[4] == fifth_guess_two:
                fifth_two_list.append(i)
        if fifth_results_two == "y":
            if i[4] != fifth_guess_two:
                if i[0] == third_guess_two or i[1] == third_guess_two or i[2] == third_guess_two or i[4] == third_guess_two:
                    fifth_two_list.append(i)
print(fifth_two_list)

if len(fifth_two_list) == 1:
    print("You have solved the puzzle!")

# ---------------------------------------------------------- 3 --------------------------------------------------------

first_guess_three=input("enter your first letter of the third word: ")
first_results_three=input("enter your results (c - correct y - yellow, g - gray): ")

first_three_list =[]
if first_results_three == "g": 
    for j in fifth_two_list: 
        if first_guess_three not in j:
            first_three_list.append(j) 
for i in fifth_two_list:
    if first_guess_three in i: 
        if first_results_three == "c":
            if i[0] == first_guess_three:
                first_three_list.append(i)
        if first_results_three == "y":
            if i[0] != first_guess_three:
                if i[1] == first_guess_three or i[2] == first_guess_three or i[3] == first_guess_three or i[4] == first_guess_three:
                    first_three_list.append(i)

print(first_three_list) 

second_guess_three=input("enter your second letter: ")
second_results_three=input("enter your results (c - correct y - yellow, g - gray): ")

second_three_list =[]
if second_results_three == "g": 
    for j in first_three_list: 
        if second_guess_three not in j:
            second_three_list.append(j) 
for i in first_three_list:
    if second_guess_three in i: 
        if second_results_three == "c":
            if i[1] == second_guess_three:
                second_three_list.append(i)
        if second_results_three == "y":
            if i[1] != second_guess_three:
                if i[0] == second_guess_three or i[2] == second_guess_three or i[3] == second_guess_three or i[4] == second_guess_three:
                    second_three_list.append(i)
print(second_three_list)


third_guess_three=input("enter your third letter: ")
third_results_three=input("enter your results (c - correct y - yellow, g - gray): ")

third_three_list =[]
if third_results_three == "g": 
    for j in second_three_list: 
        if third_guess_three not in j:
            third_three_list.append(j) 
for i in second_three_list:
    if third_guess_three in i: 
        if third_results_three == "c":
            if i[2] == third_guess_three:
                third_three_list.append(i)
        if third_results_three == "y":
            if i[2] != third_guess_three:
                if i[0] == third_guess_three or i[1] == third_guess_three or i[3] == third_guess_three or i[4] == third_guess_three:
                    third_three_list.append(i)
print(third_three_list)

fourth_guess_three=input("enter your fourth letter: ")
fourth_results_three=input("enter your results (c - correct y - yellow, g - gray): ")

fourth_three_list = []
if fourth_results_three == "g": 
    for j in third_three_list: 
        if fourth_guess_three not in j:
            fourth_three_list.append(j) 
for i in third_three_list:
    if fourth_guess_three in i: 
        if fourth_results_three == "c":
            if i[3] == fourth_guess_three:
                fourth_three_list.append(i)
        if fourth_results_three == "y":
            if i[3] != fourth_guess_three:
                if i[0] == fourth_guess_three or i[1] == fourth_guess_three or i[2] == fourth_guess_three or i[4] == fourth_guess_three:
                    fourth_three_list.append(i)
print(fourth_three_list)

fifth_guess_three=input("enter your fifth letter: ")
fifth_results_three=input("enter your results (c - correct y - yellow, g - gray): ")

fifth_three_list = []
if fifth_results_three == "g": 
    for j in fourth_three_list: 
        if fifth_guess_three not in j:
            fifth_three_list.append(j) 
for i in fourth_three_list:
    if fifth_guess_three in i: 
        if fifth_results_three == "c":
            if i[4] == fifth_guess_three:
                fifth_three_list.append(i)
        if fifth_results_three == "y":
            if i[4] != fifth_guess_three:
                if i[0] == fifth_guess_three or i[1] == fifth_guess_three or i[2] == fifth_guess_three or i[4] == fifth_guess_three:
                    fifth_three_list.append(i)
print(fifth_three_list)

if len(fifth_three_list) == 1:
    print("You have solved the puzzle!")

# ---------------------------------------------------------- 4 --------------------------------------------------------

first_guess_four=input("enter your first letter of the fourth word: ")
first_results_four=input("enter your results (c - correct y - yellow, g - gray): ")

first_four_list =[]
if first_results_four == "g": 
    for j in fifth_three_list: 
        if first_guess_four not in j:
            first_four_list.append(j) 
for i in fifth_three_list:
    if first_guess_four in i: 
        if first_results_four == "c":
            if i[0] == first_guess_four:
                first_four_list.append(i)
        if first_results_four == "y":
            if i[0] != first_guess_four:
                if i[1] == first_guess_four or i[2] == first_guess_four or i[3] == first_guess_four or i[4] == first_guess_four:
                    first_four_list.append(i)

print(first_four_list) 

second_guess_four=input("enter your second letter: ")
second_results_four=input("enter your results (c - correct y - yellow, g - gray): ")

second_four_list =[]
if second_results_four == "g": 
    for j in first_four_list: 
        if second_guess_four not in j:
            second_four_list.append(j) 
for i in first_four_list:
    if second_guess_four in i: 
        if second_results_four == "c":
            if i[1] == second_guess_four:
                second_four_list.append(i)
        if second_results_four == "y":
            if i[1] != second_guess_four:
                if i[0] == second_guess_four or i[2] == second_guess_four or i[3] == second_guess_four or i[4] == second_guess_four:
                    second_four_list.append(i)
print(second_four_list)


third_guess_four=input("enter your third letter: ")
third_results_four=input("enter your results (c - correct y - yellow, g - gray): ")

third_four_list =[]
if third_results_four == "g": 
    for j in second_four_list: 
        if third_guess_four not in j:
            third_four_list.append(j) 
for i in second_four_list:
    if third_guess_four in i: 
        if third_results_four == "c":
            if i[2] == third_guess_four:
                third_four_list.append(i)
        if third_results_four == "y":
            if i[2] != third_guess_four:
                if i[0] == third_guess_four or i[1] == third_guess_four or i[3] == third_guess_four or i[4] == third_guess_four:
                    third_four_list.append(i)
print(third_four_list)

fourth_guess_four=input("enter your fourth letter: ")
fourth_results_four=input("enter your results (c - correct y - yellow, g - gray): ")

fourth_four_list = []
if fourth_results_four == "g": 
    for j in third_four_list: 
        if fourth_guess_four not in j:
            fourth_four_list.append(j) 
for i in third_four_list:
    if fourth_guess_four in i: 
        if fourth_results_four == "c":
            if i[3] == fourth_guess_four:
                fourth_four_list.append(i)
        if fourth_results_four == "y":
            if i[3] != fourth_guess_four:
                if i[0] == fourth_guess_four or i[1] == fourth_guess_four or i[2] == fourth_guess_four or i[4] == fourth_guess_four:
                    fourth_four_list.append(i)
print(fourth_four_list)

fifth_guess_four=input("enter your fifth letter: ")
fifth_results_four=input("enter your results (c - correct y - yellow, g - gray): ")

fifth_four_list = []
if fifth_results_four == "g": 
    for j in fourth_four_list: 
        if fifth_guess_four not in j:
            fifth_four_list.append(j) 
for i in fourth_four_list:
    if fifth_guess_four in i: 
        if fifth_results_four == "c":
            if i[4] == fifth_guess_four:
                fifth_four_list.append(i)
        if fifth_results_four == "y":
            if i[4] != fifth_guess_four:
                if i[0] == fifth_guess_four or i[1] == fifth_guess_four or i[2] == fifth_guess_four or i[4] == fifth_guess_four:
                    fifth_four_list.append(i)
print(fifth_four_list)

if len(fifth_four_list) == 1:
    print("You have solved the puzzle!")

# ---------------------------------------------------------- 5 --------------------------------------------------------

first_guess_five=input("enter your first letter of the fifth word: ")
first_results_five=input("enter your results (c - correct y - yellow, g - gray): ")

first_five_list =[]
if first_results_five == "g": 
    for j in fifth_four_list: 
        if first_guess_five not in j:
            first_five_list.append(j) 
for i in fifth_four_list:
    if first_guess_five in i: 
        if first_results_five == "c":
            if i[0] == first_guess_five:
                first_five_list.append(i)
        if first_results_five == "y":
            if i[0] != first_guess_five:
                if i[1] == first_guess_five or i[2] == first_guess_five or i[3] == first_guess_five or i[4] == first_guess_five:
                    first_five_list.append(i)

print(first_five_list) 

second_guess_five=input("enter your second letter: ")
second_results_five=input("enter your results (c - correct y - yellow, g - gray): ")

second_five_list =[]
if second_results_five == "g": 
    for j in first_five_list: 
        if second_guess_five not in j:
            second_five_list.append(j) 
for i in first_five_list:
    if second_guess_five in i: 
        if second_results_five == "c":
            if i[1] == second_guess_five:
                second_five_list.append(i)
        if second_results_five == "y":
            if i[1] != second_guess_five:
                if i[0] == second_guess_five or i[2] == second_guess_five or i[3] == second_guess_five or i[4] == second_guess_five:
                    second_five_list.append(i)
print(second_five_list)


third_guess_five=input("enter your third letter: ")
third_results_five=input("enter your results (c - correct y - yellow, g - gray): ")

third_five_list =[]
if third_results_five == "g": 
    for j in second_five_list: 
        if third_guess_five not in j:
            third_five_list.append(j) 
for i in second_five_list:
    if third_guess_five in i: 
        if third_results_five == "c":
            if i[2] == third_guess_five:
                third_five_list.append(i)
        if third_results_five == "y":
            if i[2] != third_guess_five:
                if i[0] == third_guess_five or i[1] == third_guess_five or i[3] == third_guess_five or i[4] == third_guess_five:
                    third_five_list.append(i)
print(third_five_list)

fourth_guess_five=input("enter your fourth letter: ")
fourth_results_five=input("enter your results (c - correct y - yellow, g - gray): ")

fourth_five_list = []
if fourth_results_five == "g": 
    for j in third_five_list: 
        if fourth_guess_five not in j:
            fourth_five_list.append(j) 
for i in third_five_list:
    if fourth_guess_five in i: 
        if fourth_results_five == "c":
            if i[3] == fourth_guess_five:
                fourth_five_list.append(i)
        if fourth_results_five == "y":
            if i[3] != fourth_guess_five:
                if i[0] == fourth_guess_five or i[1] == fourth_guess_five or i[2] == fourth_guess_five or i[4] == fourth_guess_five:
                    fourth_five_list.append(i)
print(fourth_five_list)

fifth_guess_five=input("enter your fifth letter: ")
fifth_results_five=input("enter your results (c - correct y - yellow, g - gray): ")

fifth_five_list = []
if fifth_results_five == "g": 
    for j in fourth_five_list: 
        if fifth_guess_five not in j:
            fifth_five_list.append(j) 
for i in fourth_five_list:
    if fifth_guess_five in i: 
        if fifth_results_five == "c":
            if i[4] == fifth_guess_five:
                fifth_five_list.append(i)
        if fifth_results_five == "y":
            if i[4] != fifth_guess_five:
                if i[0] == fifth_guess_five or i[1] == fifth_guess_five or i[2] == fifth_guess_five or i[4] == fifth_guess_five:
                    fifth_five_list.append(i)
print(fifth_five_list)

if len(fifth_five_list) == 1:
    print("You have solved the puzzle!")

# ---------------------------------------------------------- 6 --------------------------------------------------------

first_guess_six=input("enter your first letter of the sixth word: ")
first_results_six=input("enter your results (c - correct y - yellow, g - gray): ")

first_six_list =[]
if first_results_six == "g": 
    for j in fifth_five_list: 
        if first_guess_six not in j:
            first_six_list.append(j) 
for i in fifth_five_list:
    if first_guess_six in i: 
        if first_results_six == "c":
            if i[0] == first_guess_six:
                first_six_list.append(i)
        if first_results_six == "y":
            if i[0] != first_guess_six:
                if i[1] == first_guess_six or i[2] == first_guess_six or i[3] == first_guess_six or i[4] == first_guess_six:
                    first_six_list.append(i)

print(first_six_list) 

second_guess_six=input("enter your second letter: ")
second_results_six=input("enter your results (c - correct y - yellow, g - gray): ")

second_six_list =[]
if second_results_six == "g": 
    for j in first_six_list: 
        if second_guess_six not in j:
            second_six_list.append(j) 
for i in first_six_list:
    if second_guess_six in i: 
        if second_results_six == "c":
            if i[1] == second_guess_six:
                second_six_list.append(i)
        if second_results_six == "y":
            if i[1] != second_guess_six:
                if i[0] == second_guess_six or i[2] == second_guess_six or i[3] == second_guess_six or i[4] == second_guess_six:
                    second_six_list.append(i)

print(second_six_list)


third_guess_two=input("enter your third letter: ")
third_results_two=input("enter your results (c - correct y - yellow, g - gray): ")

third_two_list =[]
if third_results_two == "g": 
    for j in second_two_list: 
        if third_guess_two not in j:
            third_two_list.append(j) 
for i in second_two_list:
    if third_guess_two in i: 
        if third_results_two == "c":
            if i[2] == third_guess_two:
                third_two_list.append(i)
        if third_results_two == "y":
            if i[2] != third_guess_two:
                if i[0] == third_guess_two or i[1] == third_guess_two or i[3] == third_guess_two or i[4] == third_guess_two:
                    third_two_list.append(i)
print(third_two_list)

fourth_guess_two=input("enter your fourth letter: ")
fourth_results_two=input("enter your results (c - correct y - yellow, g - gray): ")

fourth_two_list = []
if fourth_results_two == "g": 
    for j in third_two_list: 
        if fourth_guess_two not in j:
            fourth_two_list.append(j) 
for i in third_two_list:
    if fourth_guess_two in i: 
        if fourth_results_two == "c":
            if i[3] == fourth_guess_two:
                fourth_two_list.append(i)
        if fourth_results_two == "y":
            if i[3] != third_guess_two:
                if i[0] == fourth_guess_two or i[1] == fourth_guess_two or i[2] == fourth_guess_two or i[4] == fourth_guess_two:
                    fourth_two_list.append(i)

print(fourth_two_list)

fifth_guess_two=input("enter your fifth letter: ")
fifth_results_two=input("enter your results (c - correct y - yellow, g - gray): ")

fifth_two_list = []
if fifth_results_two == "g": 
    for j in fourth_two_list: 
        if fifth_guess_two not in j:
            fifth_two_list.append(j) 
for i in fourth_two_list:
    if fifth_guess_two in i: 
        if fifth_results_two == "c":
            if i[4] == fifth_guess_two:
                fifth_two_list.append(i)
        if fifth_results_two == "y":
            if i[4] != fifth_guess_two:
                if i[0] == third_guess_two or i[1] == third_guess_two or i[2] == third_guess_two or i[4] == third_guess_two:
                    fifth_two_list.append(i)
print(fifth_two_list)

if len(fifth_two_list) == 1:
    print("You have solved the puzzle!")
