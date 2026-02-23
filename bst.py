class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        if n > 1:
            left = numTrees(i-1)
            right = numTrees(n-i)


s = Solution()
value = s.numTrees(2)
print(value)