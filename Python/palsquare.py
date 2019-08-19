"""
ID: fufa0001
LANG: PYTHON3
TASK: palsquare
"""
def toStr(n,base):
   convertString = "0123456789ABCDEFGHIJKLMNO"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

fin = open("palsquare.in","r")
fout = open("palsquare.out","w")

base = int(fin.readline())
for i in range(1,301):
    square = toStr(i*i,base)
    if square == square[::-1]:
        fout.write(toStr(i,base) + " " + square + "\n")

fout.close()
