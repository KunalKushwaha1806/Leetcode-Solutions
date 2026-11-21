from typing import List
from collections import defaultdict
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        tree = defaultdict(list)
        for i in range(1, n):
            tree[parent[i]].append(i)
        last_seen = {}
        new_tree = defaultdict(list)
        
        def dfs(node):
            char = s[node]
            if char in last_seen:
                parent_node = last_seen[char]
                new_tree[parent_node].append(node)
            else:
                if node != 0:
                    new_tree[parent[node]].append(node)
            previous = last_seen.get(char)
            last_seen[char] = node
            for child in tree[node]:
                dfs(child)
            if previous is None:
                del last_seen[char]
            else:
                last_seen[char] = previous
        dfs(0)
        subtree_size = [0] * n
        
        def calculate_sizes(node):
            size = 1
            for child in new_tree[node]:
                size += calculate_sizes(child)
            subtree_size[node] = size
            return size
        calculate_sizes(0)
        
        return subtree_size