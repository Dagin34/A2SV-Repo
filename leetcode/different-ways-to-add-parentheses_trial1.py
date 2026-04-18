class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        def dfs(exp):
            if exp in memo:
                return memo[exp]
            
            if exp.isdigit():
                return [int(exp)]
            
            result = []
            for i in range(len(exp)):
                if exp[i] in "+-*":
                    left = dfs(exp[:i])
                    right = dfs(exp[i+1:])
                    
                    for l in left:
                        for r in right:
                            if exp[i] == '+':
                                result.append(l + r)
                            elif exp[i] == '-':
                                result.append(l - r)
                            else:
                                result.append(l * r)
            
            memo[exp] = result
            return result
        
        return dfs(expression)