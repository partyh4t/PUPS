# my solution
s = input("enter here: ")        
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
i = 0
total = 0

while i < len(s):
        if s[i] == "I":
            if i + 1 < len(s) and (s[i + 1] == "V" or s[i + 1] == "X"):
                total -= 1
            else:
                total += 1
        elif s[i] == "V":
            total +=5
        elif s[i] == 'X':
            if i + 1 < len(s) and (s[i + 1] == "L" or s[i + 1] == "C"):
                 total -= 10  
            else:
                total +=10
        elif s[i] == 'L':
            total += 50
        elif s[i] == 'C':
            if i + 1 < len(s) and (s[i + 1] == "D" or s[i + 1] == "M"):
                 total -= 100
            else:
                total += 100
        elif s[i] == 'D':
            total += 500
        elif s[i] == 'M':
            total += 1000
        else:
                total += 0
        i += 1

print(total)


# LeetCode Solution
class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]: # this is checking if the number next in the string is larger than the previous, if it is, that means its either IV/IX, or CD/CM, as those are the only times a larger numbers will come after a smaller number.
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans




