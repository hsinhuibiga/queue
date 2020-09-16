#Open the Lock

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        from collections import deque
        bases = [1, 10, 100, 1000]
        deads = set(int(x) for x in deadends)
        start, goal = int('0000'), int(target)
        if start in deads: return -1
        if start == goal: return 0
        q = deque([(start, 0)])
        visited = set([start])
        while q:
            node, step = q.popleft()
            for i in range(0, 4):
                r = (node // bases[i]) % 10
                for j in [-1, 1]:
                    nxt = node + ((r + j + 10) % 10 - r) * bases[i]
                    if nxt == goal: return step + 1
                    if nxt in deads or nxt in visited: continue
                    q.append((nxt, step + 1))
                    visited.add(nxt)
        return -1