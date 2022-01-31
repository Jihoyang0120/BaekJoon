cnt = int(input())
number = list(map(int, input().split()))
min = number[0]
max = number[0]
for i in number[1:]:
    if max < i:
        max = i
    elif i < min:
        min = i

print(min, max)
