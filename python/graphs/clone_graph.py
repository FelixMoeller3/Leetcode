
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visitedNodes = {}

        def cloneG(node):
            if not node:
                return None
            clone = Node(node.val)
            if node not in visitedNodes:
                visitedNodes[node] = clone
            for neighbor in node.neighbors:
                if neighbor in visitedNodes:
                    clone.neighbors.append(visitedNodes[neighbor])
                else:
                    newNeighbor = cloneG(neighbor)
                    visitedNodes[neighbor] = newNeighbor
                    clone.neighbors.append(newNeighbor)
            return clone

        return cloneG(node)

if __name__ == "__main__":
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    first.neighbors = [second,fourth]
    second.neighbors = [first,third]
    third.neighbors = [second,fourth]
    fourth.neighbors = [first,third]

    sol = Solution()
    sol.cloneGraph(first)