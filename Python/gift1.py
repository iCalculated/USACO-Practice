"""
ID: fufa0001
LANG: PYTHON3
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

lines = fin.read().splitlines()

data = {}
start = int(lines[0])
for i in range(0, start):
    cash, count = lines[start+2].split()
    data[lines[start+1]] = lines[start+2:start+int(count)+3]
    start += int(count) + 2
money = {}

for key in data:
    money[key] = 0
for key, value in data.items():
    cash, count = value[0].split()
    cash = int(cash)
    count = int(count)
    if count != 0:
        money[key] += cash % count - cash
        for name in value[1:]:
            money[name] += int(cash/count)
for name in lines[1:int(lines[0])+1]:
    fout.write(f"{name} {money[name]}\n")
fout.close()
