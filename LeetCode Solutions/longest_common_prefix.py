class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for str in strs[1:]:
            while not str.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
    

# leetcode solution
class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        # sorting it makes it so, if we just compare the first and last strings in the list, we'll be able to find the most common prefix.
        v=sorted(v) 
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 