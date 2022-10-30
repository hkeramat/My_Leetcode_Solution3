from collections import defaultdict

class Solution:
    def groupAnagrams(strs):
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

        
       

s1 = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(s1))



