class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        counter = 0
        for i in range(len(s) - 1):
            if s[i] == '(' and s[i+1] == ')':
                score += 1 << counter
            counter += 1 if s[i] == '(' else -1
        return score