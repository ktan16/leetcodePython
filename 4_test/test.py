def usage_count(ladder):
  # Write your code here
  min_integrity = min(ladder)
  return min_integrity - 1

ladder = [4, 5, 5, 4, 3, 5, 4]
print(usage_count(ladder)) # Should print 2