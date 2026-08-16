class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops={'+','-','*','/'}
        stk=[]
        for i in tokens:
            if i not in ops:
                stk.append(int(i))
            if i in ops:
                    right=stk.pop()
                    left=stk.pop()
                    if i =='+':
                        res=left+right
                    elif i=='-':
                        res=left-right
                    elif i=='*':
                        res=left*right
                    elif i=='/':
                        res=int(left/right)
                    stk.append(res)
        return stk.pop()
