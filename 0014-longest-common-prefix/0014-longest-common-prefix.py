class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:

            while not word.startswith(prefix):

                prefix = prefix[:-1]

                if not prefix:
                    return ""
        
        
        return prefix
        