n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# Please write your code here.

sum_ab = []
for num1 in A:
    for num2 in B:
        sum_ab.append(num1+num2)

sum_cd = dict()
for num1 in C:
    for num2 in D:
        sum_num = num1+num2
        if sum_num in sum_cd:
            sum_cd[sum_num] +=1
        else:
            sum_cd[sum_num] = 1

ans = 0
for num in sum_ab:
    if -num in sum_cd:
        ans += sum_cd[-num]
print(ans)
