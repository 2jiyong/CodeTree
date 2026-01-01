N, G = map(int, input().split())

group = []
group_size = []

for _ in range(G):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group.append(set(nums[1:]))

# Please write your code here.
# 그룹 사이즈가 1이면 그사람은 받는다 
ans = 1
new_members = set([1])
ans_set = set([1])
while True:
    invite_members = new_members
    new_members = set()

    if len(invite_members) == 0:
        break

    for member in invite_members:
        for i in range(G):
            if group_size[i] == 0:
                continue

            if member in group[i]:
                group[i].remove(member)
                group_size[i] -= 1

            if group_size[i] == 1:
                group_size[i] = 0
                for person in group[i]:
                    new_members.add(person)

    ans += len(new_members)

print(ans)
