class Solution:
    def kthSmallest(self, matrix, k):
        pass

# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
if __name__ == '__main__':
    matrix = [
                 [1, 5, 9],
                 [10, 11, 13],
                 [12, 13, 15]
             ]
    k = 8
    ret = Solution().kthSmallest(matrix, k)
    print(ret)
