n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.
d = dict()
for i, word in enumerate(words):
    d[word] = i

for query in queries:
    if query.isdigit():
        print(words[int(query)])
    else:
        print(d[query])