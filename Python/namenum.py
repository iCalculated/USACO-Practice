"""
ID: fufa0001
LANG: PYTHON3
TASK: namenum
"""

fin = open("namenum.in","r")
fout = open("namenum.out","w")
name_dict = open("dict.txt","r")
name_dict = [name.strip() for name in name_dict.readlines()]
serial_number = fin.readline().strip()

num_dict = {
    2: [ 'A','B','C' ],
    5: [ 'J','K','L' ],
    8: [ 'T','U','V' ],
    3: [ 'D','E','F' ],
    6: [ 'M','N','O' ],
    9: [ 'W','X','Y' ],
    4: [ 'G','H','I' ],
    7: [ 'P','R','S' ]
}

index = 0

num_len = len(serial_number)
for i in range(len(name_dict)-1,-1,-1):
    if not len(name_dict[i]) == num_len:
        name_dict.pop(i)

for num in [int(num) for num in serial_number]:
    for i in range(len(name_dict)-1,-1,-1):
        if not name_dict[i][index] in num_dict[num]:
            name_dict.pop(i)
    index += 1

written = False
for name in name_dict:
    fout.write(name+"\n")
    written = True
if not written:
    fout.write("NONE\n")
fout.close()
