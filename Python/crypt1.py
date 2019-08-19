"""
ID: fufa0001
LANG: PYTHON3
TASK: crypt1
"""
fin = open("crypt1.in","r")
fout = open("crypt1.out","w")
def test_num(num, strict=True):
    if strict and (num > 999 or num < 100):
        return False
    for char in str(num):
        if char not in digits:
            return False
    return True
dig_count, digits = [line.split() for line in fin.readlines()]
digits.sort()
good = 0
for hundreds in digits:
    for tens in digits:
        for ones in digits:
            num = int(hundreds+tens+ones)
            for ten in digits:
                for one in digits:
                    first = int(one)*num
                    second = int(ten)*num
                    if test_num(first) and test_num(second) and test_num(first+second*10, strict=False):
                        good += 1
fout.write(str(good)+"\n")


