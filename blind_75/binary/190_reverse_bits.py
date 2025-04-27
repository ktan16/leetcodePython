class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for _ in range(32):  # Assuming 32-bit integer
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

n = int("00000010100101000001111010011100", 2)

ob = Solution()
print(ob.reverseBits(n))
