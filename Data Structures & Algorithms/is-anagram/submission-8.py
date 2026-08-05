class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if (len(s) != len(t)):
            return False
        
        for i in s:
            if i in s_dict:
                s_dict[i] += 1                
            else:
                s_dict[i] = 1
        
        for j in t:
            if j in t_dict:
                t_dict[j] += 1
            else:
                t_dict[j] = 1

        print(s_dict, t_dict)

        return s_dict == t_dict