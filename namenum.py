"""
ID: fufa0001
LANG: PYTHON3
TASK: namenum
"""

fin = open("namenum.in","r")
fout = open("namenum.out","w")
name_dict = open("namenum.out","w")
name_dict = name_dict.readlines().strip()
num = int(fin.readline().strip())

num_dict = {
    2: ('A','B','C')
    5: ('J','K','L')
    8: ('T','U','V')
    3: ('D','E','F')
    6: ('M','N','O')
    9: ('W','X','Y')
    4: ('G','H','I')
    7: ('P','R','S')

fout.close()
