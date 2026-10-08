class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter = 0
        final=[]
        for i in s:
            if i=="(":
                if counter>=1:
                    final.append(i)
                counter+=1        
            elif i==")":
                if counter>1:
                    final.append(i)
                counter-=1

        return "".join(final)        
                    
        