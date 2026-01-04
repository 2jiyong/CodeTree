n = int(input())
command = []
x = []

for _ in range(n):
    line = input().split()
    command.append(line[0])
    if line[0] in ["add", "remove", "find", "lower_bound", "upper_bound"]:
        x.append(int(line[1]))
    else:
        x.append(0)


from sortedcontainers import SortedSet
# Please write your code here.
s = SortedSet()

for i in range(n):
    com = command[i]
    num = x[i]

    if com == "add":
        s.add(num)
    if com == "remove":
        s.remove(num)
    if com == "find":
        if num in s:
            print("true")
        else:
            print("false")
    if com == "lower_bound":
        target = s.bisect_left(num)
        if target >= len(s):
            print("None")
        else: 
            print(s[s.bisect_left(num)])
    if com == "upper_bound":
        target = s.bisect_right(num)
        if target >= len(s):
            print("None")
        else: 
            print(s[s.bisect_right(num)])
    if com == "largest":
        if s:
            print(s[-1])
        else:
            print("None")
    if com == "smallest":
        if s:
            print(s[0])
        else:
            print("None")
