def theFinalProblem(target):
    # Write your code here
	minimumFlips = 0
	zero = '0'
	one = '1'

	start = [0] * len(target)


	for i in range(len(target)):
		if int(target[i]) != start[i]:
			if target[i] == one:
				start[i] = 1
			elif target[i] == zero:
				start[i] = 0

			minimumFlips += 1

			for k in range(i + 1, len(target)):
				if start[k] == 0:
					start[k] = 1
				elif start[k] == 1:
					start[k] = 0

	return minimumFlips

target = "0011"
print(theFinalProblem(target))
