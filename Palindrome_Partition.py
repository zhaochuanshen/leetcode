'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
'''

class Solution:
    #this is not my solution
    def partition(self, s):
        result = []
        self.partitionRecur(result, [], s, 0)
        return result
        
    def partitionRecur(self, result, current, s, i):
        if i == len(s):
            result.append(current)
        else:
            for j in range(i, len(s)):
                if self.isPalindrome(s[i: j + 1]):
                    self.partitionRecur(result, current + [s[i: j + 1]], s, j + 1)
                
    def isPalindrome(self, s):
        for i in range(len(s) / 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True
        
