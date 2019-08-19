"""
ID: fufa0001
LANG: PYTHON3
TASK: combo
"""

fin = open("combo.in","r")
fout = open("combo.out","w")

dials, *combos = fin.readlines()
dials = int(dials)
combos = [list(map(int,combo.split())) for combo in combos]
first_diff = min(abs(combos[0][0] - combos[1][0]), abs(dials-2*max(combos[0][0],combos[1][0])+combos[0][0]+combos[1][0]))
second_diff = min(abs(combos[0][1] - combos[1][1]), abs(dials-2*max(combos[0][1],combos[1][1])+combos[0][1]+combos[1][1]))
third_diff = min(abs(combos[0][2] - combos[1][2]), abs(dials-2*max(combos[0][2],combos[1][2])+combos[0][2]+combos[1][2]))
subtract = 0
if first_diff < 5 and second_diff < 5 and third_diff < 5:
    subtract = (5 - first_diff)*(5 - second_diff)*(5 - third_diff)


if dials >= 5:
    fout.write(str(250 - subtract) + "\n")
else:
    fout.write(str(dials**3) + "\n")

fout.close()

