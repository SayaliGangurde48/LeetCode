# Problem: Plus One
# -----------------------------------------
# You are given a large integer represented as an integer array `digits`,
# where each digits[i] is the i-th digit of the integer.
#
# The digits are ordered from most significant to least significant
# (left to right).
#
# The large integer does not contain any leading zeros.
#
# Task:
# Increment the large integer by one and return the resulting array of digits.
#
# Examples:
# Input: digits = [1, 2, 3]
# Output: [1, 2, 4]
#
# Input: digits = [4, 3, 2, 1]
# Output: [4, 3, 2, 2]
#
# Input: digits = [9]
# Output: [1, 0]
#
# Constraints:
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain leading zeros.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)

        # Traverse digits from right to left
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        # If all digits were 9
        return [1] + digits


# Sample Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))   # [1, 2, 4]
    print(solution.plusOne([4, 3, 2, 1])) # [4, 3, 2, 2]
    print(solution.plusOne([9]))         # [1, 0]
