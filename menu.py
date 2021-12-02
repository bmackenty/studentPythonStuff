import os

while True:
    print("1. this is for choice 1")
    print("2. this is for choice 2")
    print("3. this is for choice 3")
    print("4. this is for choice 4")
    print("5. this is for choice 5")
    print("q. Quit")
    print("="*25)
    choice = input("Enter a choice: ")
    if choice == "q":
        break
    if choice == "1": 
        print("I'm doing stuff for choice 1")
        any_key = input("Press enter to continue...")
        os.system("clear")
    elif choice == "2":
        print("I'm doing stuff for choice 2")
        any_key = input("Press enter to continue...")
        os.system("clear")

    elif choice == "3":
        print("I'm doing stuff for choice 3")
        any_key = input("Press enter to continue...")
        os.system("clear")
