a = []
n = int(input())

for i in range(n):
    a.append(list(map(int, input().split())))


for q in range(n):
    sum = 0
    for i in range(len(a[q])-1):
        sum = sum + a[q][(i+1)]
        average = (sum / (len(a[q]) - 1))
    above = 0
    for i in range(len(a[q])-1):
        if average < a[q][(i+1)]:
            above += 1
    print('{:.3f}'.format(round((above/(len(a[q])-1))*100, 3)), "%", sep="")
