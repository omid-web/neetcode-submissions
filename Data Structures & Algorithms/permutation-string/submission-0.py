class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = defaultdict(int)
        window_count = defaultdict(int)

        for c1 in s1:
            s1_count[c1] += 1
        
        for i in range(len(s1)):
            window_count[s2[i]] += 1
        
        if window_count == s1_count:
            return True

        for r in range(len(s1), len(s2)):
            window_count[s2[r]] += 1
            left_char = s2[r - len(s1)]
            window_count[left_char] -= 1
            
            if window_count[left_char] == 0:
                del window_count[left_char]
            if s1_count == window_count:
                return True
            
        return False
            