class Solution:
    def checkString(self, s: str) -> bool:
        status=True
        for char in s:
            if char=="a" and status:
                continue
            if char=="b":
                status=False
            if char=="a" and status==False:
                return False
        return True 
        