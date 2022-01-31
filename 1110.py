n = int(input())
newNum = n
cnt = 0
while(True):
    a = newNum // 10
    b = newNum % 10
    c = (a + b) % 10
    newNum = (b * 10) + c
    cnt = cnt + 1
    if(n == newNum):
        break

print(cnt)
