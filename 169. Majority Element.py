from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        # Boyer-Moore Voting Algorithm
        for num in nums:
            if count == 0:  # Pick a new candidate when count is 0
                candidate = num
            count += (1 if num == candidate else -1)  # Update the count based on the comparison
        
        # Verification step: Check if the candidate is actually the majority element
        if nums.count(candidate) > len(nums) // 2:
            return candidate
        else:
            return -1  # If no majority element, return -1 (This is just for generic cases)
"""
Step | Current Num | Candidate Before | Count Before | Action | New Candidate | New Count
-------------------------------------------------------------------------------------
   1 |            2 |               None |            0 | Pick new candidate |            2 |         1
   2 |            3 |                 2 |            1 |    Decrease count |            2 |         0
   3 |            4 |                 2 |            0 | Pick new candidate |            4 |         1
   4 |            5 |                 4 |            1 |    Decrease count |            4 |         0
   5 |            5 |                 4 |            0 | Pick new candidate |            5 |         1
   6 |            6 |                 5 |            1 |    Decrease count |            5 |         0
   7 |            6 |                 5 |            0 | Pick new candidate |            6 |         1
   8 |            6 |                 6 |            1 |    Increase count |            6 |         2
   9 |            6 |                 6 |            2 |    Increase count |            6 |         3
  10 |            6 |                 6 |            3 |    Increase count |            6 |         4
  11 |            6 |                 6 |            4 |    Increase count |            6 |         5
  12 |            6 |                 6 |            5 |    Increase count |            6 |         6
  13 |            6 |                 6 |            6 |    Increase count |            6 |         7
  14 |            7 |                 6 |            7 |    Decrease count |            6 |         6
  15 |            8 |                 6 |            6 |    Decrease count |            6 |         5
  16 |            9 |                 6 |            5 |    Decrease count |            6 |         4

📌 Final Candidate = 6

Final Majority Element: -1
"""
