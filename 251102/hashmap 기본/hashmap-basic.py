n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

# Please write your code here.
d = {}

for command in commands:
    if command[0] == "add":
        d[command[1]] = command[2]
    if command[0] == "find":
        if command[1] in d:
            print(d[command[1]])
        else:
            print("None")
    if command[0] == "remove":
        d.pop(command[1])
