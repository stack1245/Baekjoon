import sys

input = sys.stdin.readline

n = int(input())
trie = {}

for _ in range(n):
    data = input().split()
    k = int(data[0])
    node = trie
    for i in range(1, k + 1):
        if data[i] not in node:
            node[data[i]] = {}
        node = node[data[i]]


def dfs(node, depth):
    for key in sorted(node.keys()):
        print("--" * depth + key)
        dfs(node[key], depth + 1)


dfs(trie, 0)
