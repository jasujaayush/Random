class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        queue = ['0000']
        visited = set()
        deadends = set(deadends)
        moves = 0
        while queue:
            new_queue = []
            for state in queue:
                if (state in deadends) or (state in visited):
                    continue
                
                if state == target:
                    return moves
                visited.add(state)
                for i,c in enumerate(state):
                    for delta in [1,-1]:
                        new_state = state[:i] + str((int(c) + delta)%10) + state[i+1:]
                        new_queue.append(new_state)
            queue = new_queue
            moves += 1
        return -1
        
