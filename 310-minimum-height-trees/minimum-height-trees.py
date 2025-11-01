from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]  # single node case

        # Build adjacency list
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        # Initialize first layer of leaves
        leaves = [i for i in range(n) if len(adj[i]) == 1]

        # Trim leaves until 2 or fewer nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves
