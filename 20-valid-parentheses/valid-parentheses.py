class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash_map={")":"(",
        "]":"[",
        "}":"{",
        }
        for key in s:
            if key in hash_map:
                if stack and stack[-1]==hash_map[key]:
                    stack.pop()

                
                else:
                    return False
            else:
                stack.append(key)
        return True if not stack else False
