import sys
from bisect import bisect_right

input = sys.stdin.readline

class MergeSortTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [[] for _ in range(4 * self.n)]
        self.build(arr, 1, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = [arr[start]]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node, start, mid)
            self.build(arr, 2 * node + 1, mid + 1, end)
            self.tree[node] = sorted(self.tree[2 * node] + self.tree[2 * node + 1])
    
    def count_less_equal(self, node, start, end, left, right, val):
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return bisect_right(self.tree[node], val)
        mid = (start + end) // 2
        return (self.count_less_equal(2 * node, start, mid, left, right, val) +
                self.count_less_equal(2 * node + 1, mid + 1, end, left, right, val))
    
    def query(self, left, right, k):
        lo, hi = -10**9, 10**9
        while lo < hi:
            mid = (lo + hi) // 2
            if self.count_less_equal(1, 0, self.n - 1, left, right, mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

n, m = map(int, input().split())
a = list(map(int, input().split()))

tree = MergeSortTree(a)

for _ in range(m):
    i, j, k = map(int, input().split())
    print(tree.query(i - 1, j - 1, k))
