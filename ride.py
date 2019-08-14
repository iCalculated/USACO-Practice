"""
ID: fufa0001
LANG: PYTHON3
TASK: ride
"""
import string
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
ufo,group = fin.read().splitlines()
ufo = ufo.strip()
group = group.strip()
ufo_num = 1
for char in ufo:
    #print(f"{char}: {string.ascii_uppercase.index(char)}")
    ufo_num *= string.ascii_uppercase.index(char)+1
group_num = 1
for char in group:
    #print(f"{char}: {string.ascii_uppercase.index(char)}")
    group_num *= string.ascii_uppercase.index(char)+1
if group_num % 47 == ufo_num % 47:
    #print("GO")
    fout.write("GO\n")
else:
    fout.write("STAY\n")
fout.close()

