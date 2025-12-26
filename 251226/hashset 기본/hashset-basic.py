n = int(input())
commands = []
x = []
for _ in range(n):
    cmd, val = input().split()
    commands.append(cmd)
    x.append(int(val))

# Please write your code here.
s = set()
for i in range(10):
    if c == "add":
        s.add(x[i])
    if c == "remove":
        s.remove(x[i])
    if c == "find":
        print(x[i] in s)