def getMaximumProfit(price, profit):
    # Write your code here
    maxprofit = -1
    
    for i in range(len(price)):
        for j in range(i, len(price)):
            if price[j] > price[i]:
                for k in range(j, len(price)):
                    currprofit = 0
                    if price[k] > price[j]:
                        currprofit = profit[i] + profit[j] + profit[k]
                        maxprofit = max(currprofit, maxprofit)

    return maxprofit
    # for i in range(len(price) - 2):
    #     j, k = i + 1, i + 2
    #     currentprofit = 0
    #     if price[i] < price[j] and price[j] < price[k]:
    #         currentprofit = profit[i] + profit[j] + profit[k]
    #         maxprofit = max(maxprofit, currentprofit)

def getMinimumCost(arr):
    # Write your code here
    currcost = 0
    diff = 0
    insertindex = 0
    insertnum = 0
    for i in range(len(arr) - 1):
        first = arr[i]
        second = arr[i + 1]
        currcost += (first - second) ** 2

        currdiff = abs(first - second)
        if diff < currdiff:
            diff = currdiff
            insertindex = i + 1
            insertnum = (first + second)//2
    
    arr.insert(insertindex, insertnum)
    
    calccost = 0
    for i in range(len(arr) - 1):
        calccost += (arr[i] - arr[i + 1]) ** 2
    

    # find arr[n] and arr[n + 1] where difference between is biggest
    # find num to insert so that cost is less

    return min(calccost, currcost)

price = [1,11,12,12,12]
profit = [2,3,4,5,6]
a = [4,7,1,4]

# print(getMaximumProfit(price, profit))
print(getMinimumCost(a))