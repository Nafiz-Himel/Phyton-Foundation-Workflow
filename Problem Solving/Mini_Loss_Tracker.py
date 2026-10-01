n = int(input());target = float(input())
total = 0.0
for i in range(n):
    total += float(input())
if (total/n) <= target:
    print("PASS")
else:
    print("RETRY")