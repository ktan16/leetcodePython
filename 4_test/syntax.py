# Python Syntax

# Variables
hello = "String"
i = 1
nums = [1, 2, 3]

# Classes
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# node = ListNode(1)
# print(node.val)
# print(node.next)
# node.val = 10
# print(node.val)

# Loops
arr = [1, 2, 3, 4]
for i in range (len(arr)):
    # range (x, y, z)
    # x = starting
    # y = ending
    # z = increment
    pass

# printing backwards
index = len(arr) - 1
while index >= 0:
    index -= 1

# Booleans
bool = True
bool = True or False
bool = True and (False and False)
bool = 2 == 1

# Max / Min
result = max(5, 2)
result = min(5, 2)

# Dicionary / HashMap
dict = {}
dict[10] = "ten"
dict["ten"] = 10
dict["ten"] += 1

if 10 in dict:
    pass

for key, value in dict.items():
    # print(str(key) + ": " + str(value))
    pass

while dict["ten"] >= 8:
    dict["ten"] -= 1

# String -> immutable
thing = "AB CD E"
split_thing = thing.split(" ") # creates array of [AB, CD, E]

for array_thing in split_thing:
    pass

result_thing = "".join(split_thing) # joins the strings -> "ABCDE"

name = "kenny"
name_arr = list(name)
name_arr[0], name_arr[1] = 'f', 'a' # swaps letters, kenny -> fanny
print("".join(name_arr))