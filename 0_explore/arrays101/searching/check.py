class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[i] * 2 == arr[j]) or (arr[i] % 2 == 0 and arr[i] / 2 == arr[j]):
                    return True
        return False


arr = [-2, 0, 10, -19, 4, 6, -8]

ob1 = Solution()
print(ob1.checkIfExist(arr))