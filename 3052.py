num_list = []
for i in range(10):
    num_list.append(input())

remainder_list = []
for i in num_list:
    remainder_list.append(int(i) % 42)

remainder_list = set(remainder_list)
print(len(remainder_list))
