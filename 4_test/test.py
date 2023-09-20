nums = [2,2,3,1,1,1]

counts = {}

for num in nums:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

print(counts)