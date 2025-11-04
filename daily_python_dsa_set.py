"""
Daily Python DSA Practice – 10 Problems + Solutions
---------------------------------------------------
Each function below includes a short description and time/space complexity.
Run this file directly to see quick sanity checks for each problem.
"""

from __future__ import annotations
from typing import List, Optional, Tuple, Dict, Deque
from collections import deque, OrderedDict
import heapq


# 1) Two Sum (Hash Map)
def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Return indices (i, j) such that nums[i] + nums[j] == target. Assume exactly one solution.
    Time: O(n), Space: O(n)
    """
    seen: Dict[int, int] = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return (seen[need], i)
        seen[x] = i
    raise ValueError("No solution")


# 2) Longest Substring Without Repeating Characters (Sliding Window)
def length_of_longest_substring(s: str) -> int:
    """
    Return length of longest substring with all unique characters.
    Time: O(n), Space: O(σ) where σ is char set size
    """
    start = 0
    best = 0
    last_index: Dict[str, int] = {}
    for i, ch in enumerate(s):
        if ch in last_index and last_index[ch] >= start:
            start = last_index[ch] + 1
        last_index[ch] = i
        best = max(best, i - start + 1)
    return best


# 3) Merge Intervals
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals.
    Time: O(n log n), Space: O(1) extra aside from output (after sort)
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return merged


# 4) Kth Largest Element in an Array (Min-Heap of size k)
def kth_largest(nums: List[int], k: int) -> int:
    """
    Return the kth largest element.
    Time: O(n log k), Space: O(k)
    """
    heap: List[int] = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        else:
            if x > heap[0]:
                heapq.heapreplace(heap, x)
    return heap[0]


# 5) Reverse a Singly Linked List
class ListNode:
    __slots__ = ("val", "next")
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:  # helpful for quick inspection
        return f"ListNode({self.val})"


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Iteratively reverse a singly linked list.
    Time: O(n), Space: O(1)
    """
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


# 6) Binary Tree Level-Order Traversal (BFS)
class TreeNode:
    __slots__ = ("val", "left", "right")
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Return values by level (BFS).
    Time: O(n), Space: O(n)
    """
    if not root:
        return []
    q: Deque[TreeNode] = deque([root])
    out: List[List[int]] = []
    while q:
        size = len(q)
        level: List[int] = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        out.append(level)
    return out


# 7) Number of Islands (DFS on Grid)
def num_islands(grid: List[List[str]]) -> int:
    """
    Count connected '1' components (4-directional).
    Time: O(m*n), Space: O(m*n) recursion worst-case
    """
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    def dfs(r: int, c: int) -> None:
        if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] != '1':
            return
        grid[r][c] = '#'
        dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)
    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count


# 8) Coin Change (Min Coins DP)
def coin_change(coins: List[int], amount: int) -> int:
    """
    Minimum coins to make `amount` (unbounded). Return -1 if impossible.
    Time: O(amount * len(coins)), Space: O(amount)
    """
    INF = amount + 1
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != INF else -1


# 9) Permutations (Backtracking)
def permute(nums: List[int]) -> List[List[int]]:
    """
    Return all permutations of nums.
    Time: O(n * n!), Space: O(n) backtracking + output
    """
    res: List[List[int]] = []
    used = [False] * len(nums)
    path: List[int] = []

    def backtrack():
        if len(path) == len(nums):
            res.append(path.copy())
            return
        for i in range(len(nums)):
            if used[i]: continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return res


# 10) LRU Cache (OOP + OrderedDict)
class LRUCache:
    """
    Least Recently Used cache with O(1) get/put using OrderedDict.
    get(key): return value or -1
    put(key, value): insert/update and evict LRU if capacity exceeded
    Time: O(1) average per operation, Space: O(capacity)
    """
    def __init__(self, capacity: int) -> None:
        self.cap = capacity
        self.od: "OrderedDict[int, int]" = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)


# --------------------------
# Quick sanity checks below
# --------------------------
if __name__ == "__main__":
    # 1) Two Sum
    assert two_sum([2,7,11,15], 9) in {(0,1), (1,0)}
    # 2) Longest substring
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    # 3) Merge intervals
    assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    # 4) Kth largest
    assert kth_largest([3,2,1,5,6,4], 2) == 5
    # 5) Reverse list
    a = ListNode(1, ListNode(2, ListNode(3)))
    rev = reverse_list(a)
    assert (rev.val, rev.next.val, rev.next.next.val) == (3,2,1)
    # 6) Level order
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), None))
    assert level_order(root) == [[1],[2,3],[4]]
    # 7) Number of islands
    g = [
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]
    assert num_islands(g) == 3
    # 8) Coin change
    assert coin_change([1,2,5], 11) == 3  # 5+5+1
    assert coin_change([2], 3) == -1
    # 9) Permutations
    ps = permute([1,2,3])
    assert sorted(ps) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
    # 10) LRU cache
    lru = LRUCache(2)
    lru.put(1,1); lru.put(2,2)
    assert lru.get(1) == 1
    lru.put(3,3)    # evicts 2
    assert lru.get(2) == -1
    lru.put(4,4)    # evicts 1
    assert lru.get(1) == -1 and lru.get(3) == 3 and lru.get(4) == 4

    print("All quick checks passed!")
