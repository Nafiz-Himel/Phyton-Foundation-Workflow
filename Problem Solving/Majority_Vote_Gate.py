n = int(input())
count_1 =0;count_2 = 0

for i in range(n):
    str = input()
    if str == "YES":
        count_1 += 1
    else:
        count_2 += 1

if count_1 >= count_2:
    print("ACCEPT")
else:
    print("REJECT")