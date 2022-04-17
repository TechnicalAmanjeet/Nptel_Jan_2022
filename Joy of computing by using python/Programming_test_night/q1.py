nums = list(map(int, input().split()))
k = int(input())

output = []
k = k % len(nums)
for i in range(k, len(nums)):
    output.append(nums[i])

for i in range(k+1):
    output.append(nums[i])
print(output)