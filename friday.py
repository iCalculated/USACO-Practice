"""
ID: fufa0001
LANG: PYTHON3
TASK: friday
"""
fin = open('friday.in','r')
fout = open('friday.out','w')

months = [
    ("January", 31),
    ("February", 28), #29 for leap
    ("March", 31),
    ("April", 30),
    ("May", 31),
    ("June", 30),
    ("July", 31),
    ("August", 31),
    ("September", 30),
    ("October", 31),
    ("November", 30),
    ("December", 31)
]

# Starting with Saturday
days = [0,0,0,0,0,0,0]

years = int(fin.read().strip())
passed = 12
for year in range(1900,1900+years):
    for month in months:
        days[(passed+2)%7] += 1
        if month[0] == "February" and year % 4 == 0:
            if year % 100 == 0 and not year % 400 == 0:
                passed += month[1]
            else:
                passed += month[1] + 1
        else:
            passed += month[1]

fout.write(f"{days[0]} {days[1]} {days[2]} {days[3]} {days[4]} {days[5]} {days[6]}\n")
fout.close()
