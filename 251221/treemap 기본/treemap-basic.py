n = int(input())

cmd = []
k = []
v = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] == "add":
        k.append(int(line[1]))
        v.append(int(line[2]))
    elif line[0] == "remove" or line[0] == "find":
        k.append(int(line[1]))
        v.append(0)
    else:
        k.append(0)
        v.append(0)

# Please write your code here.
from sortedcontainers import SortedDict 

d = SortedDict()

for i in range(n):
    tcmd = cmd[i]
    tk = k[i]
    tv = v[i]
    if tcmd == "add":
        d[tk] = tv
    if tcmd == "remove":
        d.pop(tk)
    if tcmd == "find":
        if tk in d:
            print(d[tk])
        else:
            print("None")
    if tcmd == "print_list":
        if len(d) == 0 :
            print("None")
            continue
        for key,value in d.items():
            print(value, end= " ")
        print()
