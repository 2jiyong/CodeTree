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
    if commands[i] == "add":
        s.add(x[i])
    if commands[i] == "remove":
        s.remove(x[i])
    if commands[i] == "find":
        print(str(x[i] in s).lower())