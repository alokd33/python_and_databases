"""
Sliding Window Technique in Python
================================

A comprehensive guide to solving subarray problems using the Sliding Window technique.

Concepts:
---------
1. Sliding Window is a technique where we maintain a window of elements in an array/string:
   - Window is defined by left and right pointers
   - Window slides through the array based on certain conditions
   - Window size can be fixed or variable

2. Common Patterns:
   - Fixed Size Window: Window size remains constant
   - Variable Size Window: Window size changes based on conditions
   - Dynamic Window: Window size changes with multiple conditions
   - Multiple Windows: Using multiple windows simultaneously

3. When to Use:
   - Finding subarrays with specific sum
   - Finding longest/shortest subarray with condition
   - Finding maximum/minimum in subarrays
   - Finding substrings with specific properties
   - Finding averages in subarrays
   - Finding subarrays with unique/distinct elements

Visualization with Step-by-Step Execution:
-----------------------------------------

1. Fixed Size Window Pattern:
   Input: nums = [1, 3, 2, 6, -1, 4, 1, 8, 2], k = 5
   
   Step 1: Initialize window
   [1, 3, 2, 6, -1, 4, 1, 8, 2]
    ^-----------^
    left       right
   window_sum = 1 + 3 + 2 + 6 + -1 = 11

   Step 2: Slide window
   [1, 3, 2, 6, -1, 4, 1, 8, 2]
       ^-----------^
       left       right
   window_sum = 3 + 2 + 6 + -1 + 4 = 14

2. Variable Size Window Pattern:
   Input: nums = [2, 1, 5, 2, 3, 2], target = 7
   
   Step 1: Initialize window
   [2, 1, 5, 2, 3, 2]
    ^--------^
    left    right
   window_sum = 2 + 1 + 5 = 8 > target → move left

   Step 2: Move left
   [2, 1, 5, 2, 3, 2]
       ^-----^
       left right
   window_sum = 1 + 5 + 2 = 8 > target → move left

3. Dynamic Window Pattern:
   Input: s = "aababcabc", k = 3
   
   Step 1: Initialize window
   "a a b a b c a b c"
    ^--------^
    left    right
   unique_chars = {'a', 'b'}

   Step 2: Expand window
   "a a b a b c a b c"
    ^-----------^
    left       right
   unique_chars = {'a', 'b', 'c'}

4. Multiple Windows Pattern:
   Input: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9], k = 3
   
   Step 1: Initialize windows
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ^-----^  ^-----^
    win1     win2
   sum1 = 6, sum2 = 15
"""

from typing import List, Dict, Set
from collections import defaultdict

def find_averages_of_subarrays(nums: List[int], k: int) -> List[float]:
    """
    Find averages of all contiguous subarrays of size k.
    
    Algorithm:
    1. Initialize window sum and result list
    2. Calculate sum of first window
    3. Slide window one element at a time:
       - Subtract outgoing element
       - Add incoming element
       - Calculate and store average
    4. Return result list
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example:
    Input: nums = [1, 3, 2, 6, -1, 4, 1, 8, 2], k = 5
    Output: [2.2, 2.8, 2.4, 3.6, 2.8]
    """
    result = []
    window_sum = 0
    left = 0
    
    for right in range(len(nums)):
        window_sum += nums[right]
        
        if right >= k - 1:
            result.append(window_sum / k)
            window_sum -= nums[left]
            left += 1
    
    return result

def smallest_subarray_with_given_sum(nums: List[int], target: int) -> int:
    """
    Find length of smallest subarray with sum >= target.
    
    Algorithm:
    1. Initialize window sum and min length
    2. Expand window by moving right pointer
    3. When sum >= target:
       - Update min length
       - Shrink window from left
    4. Return min length
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example:
    Input: nums = [2, 1, 5, 2, 3, 2], target = 7
    Output: 2  # [5, 2]
    """
    min_length = float('inf')
    window_sum = 0
    left = 0
    
    for right in range(len(nums)):
        window_sum += nums[right]
        
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0

def longest_substring_with_k_distinct(s: str, k: int) -> int:
    """
    Find length of longest substring with at most k distinct characters.
    
    Algorithm:
    1. Initialize character frequency map
    2. Expand window by moving right pointer
    3. When distinct chars > k:
       - Shrink window from left
       - Update frequency map
    4. Update max length
    
    Time Complexity: O(n)
    Space Complexity: O(k)
    
    Example:
    Input: s = "araaci", k = 2
    Output: 4  # "araa"
    """
    max_length = 0
    char_freq = defaultdict(int)
    left = 0
    
    for right in range(len(s)):
        char_freq[s[right]] += 1
        
        while len(char_freq) > k:
            char_freq[s[left]] -= 1
            if char_freq[s[left]] == 0:
                del char_freq[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

def find_anagrams(s: str, p: str) -> List[int]:
    """
    Find all starting indices of p's anagrams in s.
    
    Algorithm:
    1. Create frequency map for pattern
    2. Use sliding window to match frequencies
    3. When frequencies match, store start index
    4. Return list of start indices
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0, 6]  # "cba" and "bac"
    """
    result = []
    p_freq = defaultdict(int)
    window_freq = defaultdict(int)
    
    for char in p:
        p_freq[char] += 1
    
    left = 0
    for right in range(len(s)):
        window_freq[s[right]] += 1
        
        if right >= len(p) - 1:
            if window_freq == p_freq:
                result.append(left)
            
            window_freq[s[left]] -= 1
            if window_freq[s[left]] == 0:
                del window_freq[s[left]]
            left += 1
    
    return result

def max_sum_subarray_of_size_k(nums: List[int], k: int) -> int:
    """
    Find maximum sum of any contiguous subarray of size k.
    
    Algorithm:
    1. Calculate sum of first window
    2. Slide window one element at a time:
       - Subtract outgoing element
       - Add incoming element
       - Update max sum
    3. Return max sum
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example:
    Input: nums = [2, 1, 5, 1, 3, 2], k = 3
    Output: 9  # [5, 1, 3]
    """
    max_sum = 0
    window_sum = 0
    left = 0
    
    for right in range(len(nums)):
        window_sum += nums[right]
        
        if right >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[left]
            left += 1
    
    return max_sum

# Example usage with visualization
if __name__ == "__main__":
    print("1. Fixed Size Window Pattern:")
    nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5
    print(f"Input: {nums}, k = {k}")
    print("Step-by-step visualization:")
    print("[1, 3, 2, 6, -1, 4, 1, 8, 2]")
    print(" ^-----------^")
    print("left       right")
    result = find_averages_of_subarrays(nums, k)
    print(f"Result: {result}\n")
    
    print("2. Variable Size Window Pattern:")
    nums = [2, 1, 5, 2, 3, 2]
    target = 7
    print(f"Input: {nums}, target = {target}")
    print("Step-by-step visualization:")
    print("[2, 1, 5, 2, 3, 2]")
    print(" ^--------^")
    print("left    right")
    result = smallest_subarray_with_given_sum(nums, target)
    print(f"Result: {result}\n")
    
    print("3. Dynamic Window Pattern:")
    s = "araaci"
    k = 2
    print(f"Input: {s}, k = {k}")
    print("Step-by-step visualization:")
    print("a r a a c i")
    print("^--------^")
    print("left    right")
    result = longest_substring_with_k_distinct(s, k)
    print(f"Result: {result}\n")
    
    print("4. Multiple Windows Pattern:")
    s = "cbaebabacd"
    p = "abc"
    print(f"Input: s = {s}, p = {p}")
    print("Step-by-step visualization:")
    print("c b a e b a b a c d")
    print("^-----^")
    print("window")
    result = find_anagrams(s, p)
    print(f"Result: {result}\n")
    
    print("5. Maximum Sum Subarray:")
    nums = [2, 1, 5, 1, 3, 2]
    k = 3
    print(f"Input: {nums}, k = {k}")
    print("Step-by-step visualization:")
    print("[2, 1, 5, 1, 3, 2]")
    print(" ^-----^")
    print("left  right")
    result = max_sum_subarray_of_size_k(nums, k)
    print(f"Result: {result}")
