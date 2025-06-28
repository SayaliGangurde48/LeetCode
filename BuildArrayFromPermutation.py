# LeetCode Problem 1920: Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/

# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]].

# Example:
# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]

class Solution:
    def buildArray(self, nums):
        n = len(nums)
        
        # Step 1: Encode new values into existing array
        for i in range(n):
            nums[i] = nums[i] + (nums[nums[i]] % n) * n

        # Step 2: Extract the new values
        for i in range(n):
            nums[i] = nums[i] // n

        return nums
# This is a small update for learning GitHub pull requests.
# This is a small update for pull request practice.


