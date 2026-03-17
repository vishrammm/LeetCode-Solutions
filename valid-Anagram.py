#Approach 1
#Time Complexity: O(N log N)
#Space Complexity: O(N)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
    
    
    
#Approach 2
#Time Complexity: O(N)
#Space Complexity: O(N)

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)
    
    
    #Approach 3
    #Time Complexity: O(N)
    #Space Complexity: O(N)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            count[c] = count.get(c,0) + 1

        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1

        return True
       