from collections import defaultdict

tuple_list = [("a", 10), ("b", 4), ("c", 7), ("a", 8), ("c", 9)]

grouped_data = defaultdict(list)

for key, val in tuple_list:
    grouped_data[key].append(val)

print(grouped_data)