"""
ID: fufa0001
LANG: PYTHON3
TASK: barn1
"""

fin = open("barn1.in","r")

stats, *stalls = fin.readlines()
max_boards, stall_count, cows = [int(i) for i in stats.split()]

fout = open("barn1.out","w")
if max_boards < cows:
    stalls = list(map(int, stalls))
    stalls.sort()
    covered = stalls[-1] - stalls[0] + 1
    diff = []
    for i in range(0, len(stalls)-1):
        diff.append(stalls[i+1]-stalls[i])
    diff.sort(reverse=True)
    for i in range(0,max_boards-1):
        covered -= diff[i] - 1
    fout.write(str(covered) + "\n")
else:
    fout.write(str(cows) + "\n")


fout.close()
