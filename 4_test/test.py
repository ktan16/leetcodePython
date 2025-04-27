
# def playSegments(coins):
# 	min_plays = 10**18

# 	for i in range(len(coins)):
# 		p1_arr = coins[0:i]
# 		p2_arr = coins[i:len(coins)]

# 		p1_score = p1_arr.count(1) - p1_arr.count(0)
# 		p2_score = p2_arr.count(1) - p2_arr.count(0)

# 		if p1_score > p2_score:
# 			min_plays = min(min_plays, i)
		
# 	return min_plays

def playSegments(coins):
    # calculate initial scores
    p1_score = 0
    p2_score = coins.count(1) - coins.count(0)
    
    # if p1 wins at 0 segments, return 0 segments
    if p1_score > p2_score:
        return 0
    
    # loop through coins, starting at 1 to indicate index[0] = 1 play
    for i in range(1, len(coins)):
        # if this coin is a 1, add to p1 score and subtract from p2 score
        if coins[i - 1] == 1:
            p1_score += 1
            p2_score -= 1
        # otherwise do opposite
        else:
            p1_score -= 1
            p2_score += 1
        
        # return this play if p1 is scoring higher than p2
        # because it is the minimum
        if p1_score > p2_score:
            return i

coins = [1, 0, 0, 0, 1, 0]

print(playSegments(coins))