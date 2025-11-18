string = input()

# Please write your code here.
d = dict()
for i in range(len(string)):
    if string[i] in d:
        d[string[i]] += 1
    else:
        d[string[i]] = 1

ans = "None"
for k,v in d.items():
    if v == 1:
        ans = k
        break

print(ans)