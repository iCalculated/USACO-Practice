"""
ID: fufa0001
LANG: PYTHON3
TASK: dualpal
"""

def toStr(n,base):
   convertString = "0123456789"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

fin = open("dualpal.in","r")
amount, start = [int(i) for i in fin.readline().split()]

pals = []
while len(pals) < amount:
    start += 1
    working_bases = 0
    for i in range(2,11):
        base_conv = toStr(start, i)
        if base_conv == base_conv[::-1]:
            working_bases += 1
        if working_bases == 2:
            pals.append(start)
            break;

fout = open("dualpal.out","w")
for pal in pals:
    fout.write(str(pal) + "\n")

fout.close() 
