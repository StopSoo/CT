# https://www.acmicpc.net/problem/2475

# 내 답안
numbers = list(map(int, input().split()))
print(sum([num ** 2 for num in numbers]) % 10)