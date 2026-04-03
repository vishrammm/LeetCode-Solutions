import bisect

class Solution(object):
    def maxWalls(self, robots, distance, walls):
        """
        :type robots: List[int]
        :type distance: List[int]
        :type walls: List[int]
        :rtype: int
        """
        # Pair up robots with their distances and sort them by position
        combined = sorted(zip(robots, distance))
        pos = [c[0] for c in combined]
        d = [c[1] for c in combined]
        
        # Sort walls to allow binary search
        walls.sort()
        
        # Helper function to count walls in a closed interval [L, R]
        def count_walls(L, R):
            if L > R: 
                return 0
            idx_L = bisect.bisect_left(walls, L)
            idx_R = bisect.bisect_right(walls, R)
            return max(0, idx_R - idx_L)

        n = len(pos)
        
        # Base case for the 0-th robot
        base_0 = count_walls(pos[0], pos[0])
        prev_0 = base_0 + count_walls(pos[0] - d[0], pos[0] - 1) # 0 shoots Left
        prev_1 = base_0                                          # 0 shoots Right
        
        for i in range(1, n):
            # Walls exactly at the robot's position are unconditionally destroyed
            base_i = count_walls(pos[i], pos[i])
            
            L_i = pos[i-1]
            R_i = pos[i]
            
            # Range A: covered if robot i-1 shoots Right
            L_A = L_i + 1
            R_A = min(L_i + d[i-1], R_i - 1)
            valid_A = L_A <= R_A
            
            # Range B: covered if robot i shoots Left
            L_B = max(R_i - d[i], L_i + 1)
            R_B = R_i - 1
            valid_B = L_B <= R_B
            
            count_A = count_walls(L_A, R_A) if valid_A else 0
            count_B = count_walls(L_B, R_B) if valid_B else 0
            
            # Handle intersection if both i-1 shoots Right and i shoots Left
            intersect_L = max(L_A, L_B)
            intersect_R = min(R_A, R_B)
            if valid_A and valid_B and intersect_L <= intersect_R:
                count_intersect = count_walls(intersect_L, intersect_R)
            else:
                count_intersect = 0
                
            # Wall counts between i-1 and i for all 4 state permutations
            cost_LL = count_B
            cost_RL = count_A + count_B - count_intersect
            cost_LR = 0
            cost_RR = count_A
            
            # Transition DP states
            curr_0 = max(prev_0 + cost_LL, prev_1 + cost_RL) + base_i
            curr_1 = max(prev_0 + cost_LR, prev_1 + cost_RR) + base_i
            
            prev_0, prev_1 = curr_0, curr_1
            
        # Final answer considers the right-side coverage of the very last robot (if it shoots right)
        ans = max(prev_0, prev_1 + count_walls(pos[n-1] + 1, pos[n-1] + d[n-1]))
        return ans