class Solution:
    def maxCoins(self, nums):
        """
        Calculate the maximum coins that can be obtained by bursting the balloons wisely.

        :param nums: A list of integer representing the number of balloons
        :type nums: List[int]
        :return: The maximum coins obtained
        :rtype: int
        """
        # Add a balloon with value 1 to each end of the list to simplify calculations
        nums = [1] + nums + [1]
        # Calculate the length of the new nums list
        n = len(nums)
        # Initialize the dp (Dynamic Programming) table with zeros
        dp = [[0] * n for _ in range(n)]

        # Fill the dp table
        # l represents the length of the range we're considering
        for l in range(2, n):
            # i represents the start of the range
            for i in range(n - l):
                # j represents the end of the range
                j = i + l
                # Test each possible position 'k' for the balloon to burst last in the range (i, j)
                for k in range(i + 1, j):
                    # Calculate the maximum coins by adding the coins obtained from bursting the current balloon
                    # (nums[i]*nums[k]*nums[j]) plus the maximum coins from the two subranges (i, k) and (k, j)
                    dp[i][j] = max(
                        dp[i][j],  # Current max coins for range (i, j)
                        dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]  # Max coins if balloon k is burst last
                    )
        # The maximum coins obtained will be in the top right corner of the dp table
        return dp[0][-1]
