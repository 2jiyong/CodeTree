n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

# Please write your code here.
s = set(arr1)

for num in arr2:
    if num in s:
        print(1, end=" ")
    else:
        print(0, end=" ")