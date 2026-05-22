class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for j in range(len(prefix)):
            for i in range(1,len(strs)):
                if prefix in strs[i]:
                    continue
                else:
                    prefix = prefix[:-1]
                    break
        return prefix