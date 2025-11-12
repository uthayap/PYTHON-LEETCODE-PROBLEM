class Solution(object):
    def longestValidParentheses(self, s):
        dp, stack = [0]*(len(s)+1), []
        res = 0
        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack:
                idx = stack.pop()
                dp[i+1] = dp[idx] + (i-idx+1)
                res = max(res, dp[i+1])
        return res