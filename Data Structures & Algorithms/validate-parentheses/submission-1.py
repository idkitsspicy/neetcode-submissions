class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        d={')':'(','}':'{',']':'['}
        for i in s:
            if i not in d:
                stk.append(i)
            else:
                if not stk:
                    return False
                else:
                    x=stk.pop()
                    if x!=d[i]:
                        return False
        return not stk
                    
                

