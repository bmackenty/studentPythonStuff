# This program makes a list of random names, ID numbers and email's which resemble the actual username
# The purpose of this file is to create dummy data which can be used to run benchmark testing on databases 
# This code is a horribly and quickly implemented hack to solve a problem for a student.
#
# the names were taken from here: https://stackoverflow.com/questions/1803628/raw-list-of-person-names
# The technique I used to replace odd characters is so, so, so very ugly and silly
# however, the actual code isn't mine. https://stackoverflow.com/questions/3411771/multiple-character-replace-with-python
#  

# TODO: the ID's can possibly duplicate. fix to ensure they are unique. 


import random

# change this to full path:
fname = 'firstname.txt'
lname = 'lastname.txt'

valid_tld_domains = [".com",".org",".eu",".net",".pl",".in",".pk"]
valid_domains = ["gmail","yahoo","icloud","aol","hotmail"]

with open(fname) as f:
    first_names = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
first_names = [x.strip() for x in first_names] 

with open(lname) as f:
    last_names = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
last_names = [x.strip() for x in last_names]

capitalized_last_names = []
for i in last_names:
    capitalized_last_names.append(i.capitalize())

capitalized_first_names = []
for i in first_names:
    capitalized_first_names.append(i.capitalize())


# change line below to however many addresses you want. It's currently set to a million:
for i in range(0,1000000):
    last_name = random.choice(capitalized_first_names)
    first_name = random.choice(capitalized_first_names)
    domain = random.choice(valid_domains)
    tld = random.choice(valid_tld_domains)

    #name 
    fullname = (first_name+" "+last_name)
    for fn in ['(',')','\'',',']:
        if fn in fullname:
            fullname=fullname.replace(fn,"")

    #id number 
    id_number = random.randrange(1000000,5000000)

    # email     
    email = (first_name[0],last_name,"@",domain,tld)
    email = str(email)
    for ch in ['(',')','\'',' ',',']:
        if ch in email:
            email=email.replace(ch,"")
    email = email.lower()        
    print(fullname,",",id_number,",",email)

# When running the code, you probably want to type something like: 
# $ fakeUserCSV.py > my_fake_user_file.csv
