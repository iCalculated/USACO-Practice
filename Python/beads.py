"""
ID: fufa0001
LANG: PYTHON3
TASK: beads
"""
fin = open('beads.in','r')
fout = open('beads.out','w')

length, order = fin.readlines()
length = int(length)
order = order

max_length = 1
for i in range(0, length):
    current_length = 0
    forward = i
    backward = i - 1

    while current_length < max_length and order[forward%length] == "w":
        current_length += 1
        forward += 1

    forward_color = order[forward%length]
    while current_length < length and (order[forward%length] == forward_color or order[forward%length] == "w"):
        current_length += 1
        forward += 1

    while current_length < length and order[backward%length] == "w":
        current_length += 1
        backward -= 1
    backward_color = order[backward%length]
    while current_length < length and (order[backward%length] == backward_color or order[backward%length] == "w"):
        current_length += 1
        backward -= 1

    if current_length > max_length:
        max_length = current_length

if max_length > length:
    max_length = length

fout.write(str(max_length) + "\n")
fout.close()
