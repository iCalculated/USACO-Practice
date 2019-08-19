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
first_diff = min(abs(combos[0][0] - combos[1][0]), abs(combos[0][0] + combos[1][0] - dials + 2)%dials)
second_diff = min(abs(combos[0][1] - combos[1][1]), abs(combos[0][1] + combos[1][1] - dials + 2)%dials)
third_diff = min(abs(combos[0][2] - combos[1][2]), abs(combos[0][2] + combos[1][2] - dials + 2)%dials)
subtract = 0
if first_diff < 5 and second_diff < 5 and third_diff < 5:
    subtract = (5 - first_diff)*(5 - second_diff)*(5 - third_diff)


if dials >= 5:
    fout.write(str(250 - subtract) + "\n")
else:
    fout.write(str(dials**3) + "\n")

fout.close()

