# None = null
# and = &&
# or = ||

#########
# LOOPS #
#########

for i in range(4): # 0 -> 4
    print(i)

for i in range(2, 6): # 2 -> 5
    print(i)

for i in range (5, 1, -1): # 5 -> 1
    print(i)

################
# ARRAYS/LISTS #
################

arr = [1,2,3]

arr.append(4)
arr.pop() 
arr.insert(1, 7) # insert 7 at index 1
arr[1] = 0

n = 5
arr = [1] * n # initialize array of size n with values 1

arr[-1] # last value in array

arr = [1,2,3,4]
print(arr[1:3]) # sublists, prints [2,3], last index non-inclusive

nums = [0,1,2]
for i in range(len(nums)):
    print(nums[i])

for num in nums:
    print(num)

for i, num in enumerate(nums): # loop through array with index and value
    print(i, n)

nums1 = [1,3,5]
nums2 = [2,4,6]

for n1, n2 in zip(nums1, nums2): # unpacking multiple arrays
    print(n1, n2)

arr = [1,2,3]
arr.reverse() # reverse an array
arr.sort() # sorts numerically/alphabetically
arr.sort(reverse = True) # sorts descending
arr.sort(key = lambda x: len(x)) # lambda function (no name), map all values of array to x and return length of x from mapping

###########
# STRINGS #
###########

s = 'abc'
print(s[0:2]) # slicing, output 'ab'

s += 'def' # strings are immutable but can be modified, creates new string

print(int('123') + int('123')) # 246
print(str(123) + str(123)) # '123123'
# can convert int <-> str and perform operations

print(ord('a')) # ascii value

strings = ['ab', 'cd', 'ef']
print(''.join(strings)) # combine list of strings using '' delimiter

##########
# QUEUES #
##########

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)

queue.popleft()
queue.appendleft(1)

#############
# HASH SETS #
#############

mySet = set()
mySet.add(1)
mySet.add(2)
print(len(mySet))

print(1 in mySet)
print(2 in mySet)

mySet = {i for i in range(5)} # set comprehension

############
# HASH MAP #
############

myMap = {}

myMap['mango'] = 1
myMap['apple'] = 2
print(len(myMap))

print('mango' in myMap)
myMap.pop('mango')
print('mango' in myMap)

myMap = {'alice':88, 'bob':77}

# dict comprehension
myMap = {i: 2*i for i in range(3)} # {0:0, 1:2, 2:4}
# map i key with value 2*i

for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)

##########
# TUPLES #
##########
tup = (1,2,3) # tuples are immutable arrays

# usually used in keys for maps/sets because arrays not hashable
myMap = {(1,2):3}
print(myMap[(1,2)])

mySet.add((1,2))
print((1,2) in mySet)

# HEAPS # used for min/max
import heapq

minHeap = [] # default minheap
heapq.heappush(minHeap, 3) # no max heaps, workaround is to multiply by
heapq.heappush(minHeap, 2) # -1 whenever pushing or popping
heapq.heappush(minHeap, 4) # heapq.heappush(maxHeap, -3)

print(minHeap[0]) # min is always at index 0

while len(minHeap): # while there is stuff / minheap != 0
    print(heapq.heappop(minHeap))

arr = [2,1,8,4,5]
heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr))

#############
# FUNCTIONS #
#############

def func(n, m):
    return n*m

def pfunc(x, y):
    print(x * y)
pfunc(3,4)

print(func(3,4))

# nested functions have access to outer vars
def outer(a, b):
    c = 'c'

    def inner():
        return a + b + c
    return inner()

print(outer('a', 'b'))

# can modify objects but not reassign
# unless using nonlocal keyword
def double(arr, val): # doubles each value in array and also val
    def helper():
        # can modify array
        for i in range(len(arr)):
            arr[i] *= 2

        # val *= 2 will only modify val in the helper scope

        nonlocal val # references val outside of scope
        val *= 2

    helper()
    print(arr, val)

nums = [1,2]
val = 3
double(nums, val)

###########
# CLASSES #
###########

class MyClass:
    # Constructor
    # self is passed into every method of a class
    # in this case constructor is also taking list of numbers
    def __init__(self, nums):
        # create member variables
        self.nums = nums
        self.size = len(nums)

    # self keyword required param
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength()