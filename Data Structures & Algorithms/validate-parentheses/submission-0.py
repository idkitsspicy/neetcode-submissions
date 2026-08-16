class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={')':'(','}':'{',']':'['}
        stk=[]
        for i in s:
            if i not in hashmap:
                stk.append(i)
            else:
                if not stk:
                    return False
                else:
                    x=stk.pop()
                    if x!=hashmap[i]:
                        return False
        return not stk