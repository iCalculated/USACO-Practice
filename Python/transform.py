"""
ID: fufa0001
LANG: PYTHON3
TASK: transform
"""

def reflect(arr):
    return [row[::-1] for row in arr]

def rotate_90(arr):
    return [''.join(row) for row in list(zip(*arr[::-1]))]

def rotate_180(arr):
    return [row[::-1] for row in arr[::-1]]

def rotate_270(arr):
    return [list(row[::-1]) for row in list(zip(*arr))]

fin = open("transform.in","r")
fout = open("transform.out","w")

lines = fin.readlines()
size = int(lines[0])
before = [line.strip() for line in lines[1:1+size]]
after = [line.strip() for line in lines[1+size:]]

if rotate_90(before) == after:
    case = 1
elif rotate_180(before) == after:
    case = 2
elif rotate_270(before) == after:
    case = 3
elif reflect(before) == after:
    case = 4
elif rotate_90(reflect(before)) == after or rotate_180(reflect(before)) == after or rotate_270(reflect(before)) == after:
    case = 5
elif before == after:
    case = 6
else:
    case = 7

fout.write(str(case) + "\n")
fout.close

