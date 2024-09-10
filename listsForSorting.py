
# This program is used to generate ordered and unordered lists.
# The lists are then used for computer science students to 
# apply their understanding of standard searches and sorts. 


# the line below imports the random library, which enables us to use lots of functions with random.
import random
# the line below imports the time library, which enables us to use lots of functions with time
import time

# we need to time our program, so we are going to set the start time
start_time = time.time()

myList = []
numberToFind = 700

def unorderedList():
	# this function creates an unordered list
	for i in range(0,25):
		# the line line below simply appends a random number into our list
		myList.append(random.randrange(1,90000))
	return myList


def orderedList():
	# this function creates an ordered list
	for i in range(0,25):
		myList.append(i)
	return myList


# this is where we call the functions to make our lists
# uncomment out whichever list you want to make

unorderedList()
# orderedList()



# =========================================================
# Your different sorting algorithms will go under this line
# =========================================================


def linearSearch(list,target):
	length = len(list)
	for i in range(0,length):
		if i == target:
			return i
	return -1


def bubbleSort(list):
	swapped = True
	while swapped:
		swapped = False	
		for i in range(0,(len(list)-1)):	
			if list[i] > list[(i+1)]:
				firstNumber = list[i]
				secondNumber = list[(i+1)]
				list[i] = secondNumber
				list[(i+1)] = firstNumber
				swapped=True
	return list


# =========================================================
# Your different sorting algorithms will go above this line
# =========================================================


# =========================================================
# The lines below call a function. For sorting, we like to 
# print the unsorted list and sorted list
# =========================================================

print(myList)
print("")
print(bubbleSort(myList))


# the lines below are used only for debugging. 
# print(myList)	
# The line below should print true if our target exists in our list. 	
# print(numberToFind in myList)


print("--- %s seconds ---" % (time.time() - start_time))


#
# references
#
# I am grateful to stackoverflow for this code for timing a python program: 
# https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
