class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for l in logs:
            if l != './':
                if l!='../':
    
                    stack.append(l)
                elif stack!= []:
                    
                    stack.pop()
        return len(stack)
                
            