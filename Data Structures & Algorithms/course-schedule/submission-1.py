class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = dict()
        for pre in prerequisites:
            graph[pre[0]] = graph.get(pre[0], set())
            graph[pre[0]].add(pre[1])

        dp = {}
        def dfs(c, current):
            if c in current:
                return False
            
            if c in dp:
                return dp[c]
            
            current.add(c)
            prereq = graph.get(c, set())
            res = True
            for p in prereq:
                if not dfs(p, current.copy()):
                    res = False
                    break
            
            current.remove(c)

            dp[c] = res
            return dp[c]

        for i in range(1, 20):
            if not dfs(numCourses - i, set()):
                return False

        return True

        