import re

namecounter = 0
surnamecounter = 0
with open('student.txt') as dob:
    for row in dob:
        rowstrings = row.split()
        name = rowstrings[0] + " " + rowstrings[1]
        birthdate = rowstrings[3] + " " + rowstrings[2] + " " + rowstrings[4]
        namecounter += 1
        surnamecounter += 1
        print(f"Name: {name}" + "\n" + f"Birth date: {birthdate}")
