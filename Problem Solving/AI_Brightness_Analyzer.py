nums = input().split()
total = 0
for num in nums:
    total += int(num)

if(total/len(nums)) < 85:
    print("Dark Image")
elif (total/len(nums)) <= 170:
    print("Normal Image")
elif(total/len(nums)) >170:
    print("Bright Image")