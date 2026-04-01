import numpy as np
class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        n = len(positions)

    # Step 1: sort robots by position, but remember original index
        indices = sorted(range(n), key=lambda i: positions[i])

        stack = []          # stores original indices of R-moving robots
        healths = list(healths)  # make mutable copy

    # Step 2: process left to right by position
        for i in indices:
            if directions[i] == 'R':
                stack.append(i)
            else:  # directions[i] == 'L'
            # Fight all R robots on top of stack
                while stack:
                    top = stack[-1]  # rightmost R robot

                    if healths[top] > healths[i]:       # R wins
                        healths[top] -= 1
                        healths[i] = 0                  # L is dead
                        break
                    elif healths[top] < healths[i]:     # L wins
                        healths[i] -= 1
                        healths[top] = 0                # R is dead
                        stack.pop()
                    # L continues fighting next R on stack
                    else:                               # tie → both die
                        healths[top] = 0
                        healths[i] = 0
                        stack.pop()
                        break

    # Step 3: collect survivors in original order
        return [healths[i] for i in range(n) if healths[i] > 0]