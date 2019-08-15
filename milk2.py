"""
ID: fufa0001
LANG: PYTHON3
TASK: milk2
"""
fin = open('milk2.in','r')
fout = open('milk2.out','w')
count, *times = fin.readlines()
for i in range(0,int(count)):
    times[i]=list(map(int, times[i].split()))
times = sorted(times, key=lambda tup: tup[0])
merged = []
for higher in times:
    if not merged:
        merged.append(higher)
    else:
        lower = merged[-1]
        if higher[0] <= lower[1]:
            upper_bound = max(lower[1], higher[1])
            merged[-1] = (lower[0], upper_bound)  # replace by merged interval
        else:
            merged.append(higher)
longest_milk = 0
longest_no_milk = 0
for i in range(0,len(merged)):
    diff = merged[i][1] - merged[i][0]
    if diff > longest_milk:
        longest_milk = diff
    if i != len(merged) - 1:
        diff = merged[i+1][0] - merged[i][1] 
        if diff > longest_no_milk:
            longest_no_milk = diff
fout.write(str(longest_milk) + " " + str(longest_no_milk) + "\n")
fout.close()
