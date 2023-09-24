#
# Complete the 'subsetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def subsetA(arr):
    # Write your code here
    s_arr = sorted(arr, reverse = True)

    subset_a = []
    sum_a = 0

    for num in s_arr:
        if sum_a <= sum(arr) - sum_a: # subset_b = sum(arr) - subset_a
            subset_a.append(num)
            sum_a += num
        else:
            break
    
    return sorted(subset_a)

#
# Complete the 'getNumber' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_SINGLY_LINKED_LIST binary as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def getNumber(binary):
    # Write your code here
    current = binary
    bn = []
    while current:
        bn.append(current.data)
        current = current.next
    
    num = 0
    power = 0
    
    for i in range(len(bn) - 1, -1, -1):
        if bn[i] == 1:
            num += 2 ** power
        power += 1

    return num
    
arr = [5,3,2,4,1,2]
print(subsetA(arr))
