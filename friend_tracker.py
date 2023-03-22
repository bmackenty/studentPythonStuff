import os
os.system("clear")

# the code below will create a file if it doesn't exist:
try:
    f = open("friends.txt", "r")
    f.close()
except FileNotFoundError:
    print("I couldn't find friends.txt, so I created it for you.")
    f = open("friends.txt", "w")
    f.close()


# add a friend to the list:
def add_friend(friend):
    f = open("friends.txt", "a")
    f.write(friend + "\n")


# open file for reading:
def list_friends():
    f = open("friends.txt", "r")
    print(f.read())

# add some friends:
add_friend("Emily")
add_friend("Jana")
add_friend("Jose")
add_friend("Edo")
add_friend("Pawel")

# list all friends:
list_friends()
