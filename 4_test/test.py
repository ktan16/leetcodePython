arr = [4,7,1,4]

for i in range(len(arr) - 1):
    first = arr[i]
    second = arr[i + 1]

    mid = (first + second)//2
    print(mid)

