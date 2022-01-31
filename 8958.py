a = []
cnt = int(input())
for i in range(cnt):
    a.append(input())

for q in range(cnt):
    score = 0
    accum = -1
    for i in range(len(a[q])):
        while(a[q][i] == "O"):
            score += 1
            accum += 1
            score = score + accum
            break
        if (a[q][i] == "X"):
            accum = -1
    print(score)
