"""
ID: fufa0001
LANG: PYTHON3
TASK: milk
"""

fin = open("milk.in","r")
reqs, *farmers = fin.readlines()

req, _ = reqs.split()
req = int(req)

farmers = map(lambda term: [int(value) for value in term.split()], farmers)
sorted_prices = sorted(farmers, key= lambda tup: tup[0], reverse=True)

price = 0

while req > 0:
    cheapest = sorted_prices.pop()
    if req - cheapest[1] > 0:
        req -= cheapest[1]
        price += cheapest[0] * cheapest[1]
    else:
        price += req * cheapest[0]
        req = 0

fout = open("milk.out","w")
fout.write(str(price) + "\n")
fout.close()
