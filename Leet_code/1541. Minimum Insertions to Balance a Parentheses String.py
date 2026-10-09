#day5
class Solution:
    def minInsertions(self, s: str) -> int:
        insertion = 0      
        open_count = 0  
        i = 0
        
        while i < len(s):
            if s[i] == '(':
                open_count += 1
                i += 1
            else:#")"
               
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 2 
                else:
                    insertion += 1
                    i += 1  

                if open_count > 0:
                    open_count -= 1
                else:
                    insertion += 1 
        return  insertion + open_count * 2  
