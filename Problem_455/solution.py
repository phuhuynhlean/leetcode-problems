class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_index = 0
        s_index = 0
        result = 0

        while g_index < len(g) and s_index < len(s):
            if (g[g_index] <= s[s_index]):
                result += 1
                g_index += 1
                s_index += 1
            else:
                s_index += 1
        return result