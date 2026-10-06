class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        adds_needed = 0
        for i in s:
            if i == "(":
                open_count+=1
            elif i==")":
                if open_count>0:
                    open_count-=1
                else:
                    adds_needed+=1
            else:
                print("worng input:")

        return adds_needed+open_count
