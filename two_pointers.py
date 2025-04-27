"""
Two Pointers Technique in Python
===============================

A comprehensive guide to solving array and string problems using the Two Pointers technique.

Concepts:
---------
1. Two Pointers is a technique where we use two pointers to traverse an array or string:
   - One pointer starts from the beginning (left)
   - Another pointer starts from the end (right)
   - They move towards each other based on certain conditions

2. Common Patterns:
   - Opposite Direction: Pointers move towards each other
   - Same Direction: Both pointers move in the same direction
   - Fast & Slow: One pointer moves faster than the other
   - Sliding Window: Maintain a window of elements
   - Three Pointers: For more complex problems

3. When to Use:
   - Finding pairs in a sorted array
   - Removing duplicates
   - Reversing arrays/strings
   - Finding subarrays with specific properties
   - Palindrome checking
   - Merging sorted arrays
   - Finding subarrays with sum
   - Finding longest substring without repeating characters

Visualization with Step-by-Step Execution:
-----------------------------------------

1. Two Sum Sorted Pattern:
   Input: nums = [1, 2, 3, 4, 5], target = 7
   
   Step 1: Initialize pointers
   [1, 2, 3, 4, 5]
    ^           ^
    left       right
   sum = 1 + 5 = 6 < target → move left

   Step 2: Move left pointer
   [1, 2, 3, 4, 5]
       ^        ^
       left    right
   sum = 2 + 5 = 7 == target → return [1, 4]

2. Remove Duplicates Pattern:
   Input: nums = [1, 1, 2, 2, 3]
   
   Step 1: Initialize pointers
   [1, 1, 2, 2, 3]
    ^  ^
    slow fast
   nums[fast] == nums[slow-1] → move fast

   Step 2: Move fast pointer
   [1, 1, 2, 2, 3]
    ^     ^
    slow  fast
   nums[fast] != nums[slow-1] → copy and move both

   Step 3: Copy and move
   [1, 2, 2, 2, 3]
       ^  ^
       slow fast

3. Longest Substring Without Repeating:
   Input: s = "abcabcbb"
   
   Step 1: Initialize window
   "a b c a b c b b"
    ^--------^
    left    right
   window = {a, b, c}

   Step 2: Move right
   "a b c a b c b b"
    ^-----------^
    left       right
   window = {a, b, c} → max_len = 3

   Step 3: Move left (duplicate found)
   "a b c a b c b b"
       ^--------^
       left    right
   window = {b, c, a}

4. Three Sum Pattern:
   Input: nums = [-1, 0, 1, 2, -1, -4]
   
   Step 1: Sort and initialize
   [-4, -1, -1, 0, 1, 2]
    ^   ^           ^
    i   left       right
   sum = -4 + -1 + 2 = -3 < 0 → move left

   Step 2: Move left
   [-4, -1, -1, 0, 1, 2]
    ^      ^        ^
    i     left     right
   sum = -4 + -1 + 2 = -3 < 0 → move left

5. Sort Colors (Dutch Flag):
   Input: nums = [2, 0, 2, 1, 1, 0]
   
   Step 1: Initialize pointers
   [2, 0, 2, 1, 1, 0]
    ^  ^           ^
    low mid       high
   nums[mid] == 0 → swap with low

   Step 2: After swap
   [0, 0, 2, 1, 1, 2]
       ^  ^     ^
       low mid  high
   nums[mid] == 2 → swap with high

6. Subarray Sum Pattern:
   Input: nums = [1, 2, 3, 4, 5], target = 9
   
   Step 1: Initialize window
   [1, 2, 3, 4, 5]
    ^--------^
    left    right
   sum = 1 + 2 + 3 = 6 < target → move right

   Step 2: Move right
   [1, 2, 3, 4, 5]
    ^-----------^
    left       right
   sum = 1 + 2 + 3 + 4 = 10 > target → move left

   Step 3: Move left
   [1, 2, 3, 4, 5]
       ^--------^
       left    right
   sum = 2 + 3 + 4 = 9 == target → return [1, 3]
"""

from typing import List, Optional, Tuple, Set

def two_sum_sorted(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Find two numbers in a sorted array that sum to target.
    
    Algorithm:
    1. Initialize left pointer at start and right at end
    2. While left < right:
       - Calculate sum of nums[left] + nums[right]
       - If sum == target: return indices
       - If sum < target: move left pointer right
       - If sum > target: move right pointer left
    3. Return None if no pair found
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example:
    Input: nums = [1, 2, 3, 4, 5], target = 7
    Output: (2, 3)  # indices of 3 and 4
    """
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

def remove_duplicates(nums: List[int]) -> int:
    """
    Remove duplicates from sorted array in-place.
    
    Algorithm:
    1. Initialize slow pointer at index 1
    2. For each element with fast pointer:
       - If nums[fast] != nums[slow-1]:
         * Copy nums[fast] to nums[slow]
         * Increment slow
    3. Return length of unique elements
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example:
    Input: nums = [1, 1, 2, 2, 3]
    Output: 3  # [1, 2, 3]
    """
    if not nums:
        return 0
    
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow

def longest_substring_without_repeating(s: str) -> int:
    """
    Find length of longest substring without repeating characters.
    
    Algorithm:
    1. Initialize left pointer and character set
    2. For each character with right pointer:
       - While character in set:
         * Remove leftmost character
         * Move left pointer right
       - Add current character to set
       - Update max length
    3. Return max length
    
    Time Complexity: O(n)
    Space Complexity: O(min(m, n)) where m is charset size
    
    Example:
    Input: "abcabcbb"
    Output: 3  # "abc"
    """
    left = 0
    max_length = 0
    char_set = set()
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.
    
    Algorithm:
    1. Sort the array
    2. For each element:
       - Use two pointers to find pairs that sum to -nums[i]
       - Skip duplicates
    3. Return all unique triplets
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Example:
    Input: nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
    """
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    
    return result

def sort_colors(nums: List[int]) -> None:
    """
    Sort array of 0s, 1s, and 2s in-place (Dutch Flag problem).
    
    Algorithm:
    1. Initialize three pointers:
       - low at start
       - mid at start
       - high at end
    2. While mid <= high:
       - If nums[mid] == 0: swap with low, move both
       - If nums[mid] == 1: move mid
       - If nums[mid] == 2: swap with high, move high left
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example:
    Input: [2, 0, 2, 1, 1, 0]
    Output: [0, 0, 1, 1, 2, 2]
    """
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

def subarray_sum(nums: List[int], target: int) -> List[int]:
    """
    Find subarray that sums to target (positive numbers only).
    
    Algorithm:
    1. Initialize left pointer and current sum
    2. For each element with right pointer:
       - Add to current sum
       - While sum > target:
         * Subtract nums[left]
         * Move left pointer right
       - If sum == target: return indices
    3. Return empty list if no subarray found
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example:
    Input: nums = [1, 2, 3, 4, 5], target = 9
    Output: [2, 3]  # indices of subarray [3, 4]
    """
    left = 0
    current_sum = 0
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum > target:
            current_sum -= nums[left]
            left += 1
            
        if current_sum == target:
            return [left, right]
    
    return []

# Example usage with visualization
if __name__ == "__main__":
    print("1. Two Sum Sorted Pattern:")
    nums = [1, 2, 3, 4, 5]
    target = 7
    print(f"Input: {nums}, target = {target}")
    print("Step-by-step visualization:")
    print("[1, 2, 3, 4, 5]")
    print(" ^           ^")
    print("left       right")
    result = two_sum_sorted(nums, target)
    print(f"Result: {result}\n")
    
    print("2. Remove Duplicates Pattern:")
    nums = [1, 1, 2, 2, 3]
    print(f"Input: {nums}")
    print("Step-by-step visualization:")
    print("[1, 1, 2, 2, 3]")
    print(" ^  ^")
    print("slow fast")
    result = remove_duplicates(nums)
    print(f"Result: {result}\n")
    
    print("3. Longest Substring Pattern:")
    s = "abcabcbb"
    print(f"Input: {s}")
    print("Step-by-step visualization:")
    print("a b c a b c b b")
    print("^--------^")
    print("left    right")
    result = longest_substring_without_repeating(s)
    print(f"Result: {result}\n")
    
    print("4. Three Sum Pattern:")
    nums = [-1, 0, 1, 2, -1, -4]
    print(f"Input: {nums}")
    print("Step-by-step visualization:")
    print("[-4, -1, -1, 0, 1, 2]")
    print(" ^   ^           ^")
    print(" i   left       right")
    result = three_sum(nums)
    print(f"Result: {result}\n")
    
    print("5. Sort Colors Pattern:")
    nums = [2, 0, 2, 1, 1, 0]
    print(f"Input: {nums}")
    print("Step-by-step visualization:")
    print("[2, 0, 2, 1, 1, 0]")
    print(" ^  ^           ^")
    print("low mid        high")
    sort_colors(nums)
    print(f"Result: {nums}\n")
    
    print("6. Subarray Sum Pattern:")
    nums = [1, 2, 3, 4, 5]
    target = 9
    print(f"Input: {nums}, target = {target}")
    print("Step-by-step visualization:")
    print("[1, 2, 3, 4, 5]")
    print(" ^--------^")
    print("left    right")
    result = subarray_sum(nums, target)
    print(f"Result: {result}")
