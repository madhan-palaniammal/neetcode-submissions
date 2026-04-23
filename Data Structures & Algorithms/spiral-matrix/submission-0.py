class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        rs = 0
        re = len(matrix)
        cs = 0
        ce = len(matrix[0])
        while rs < re and cs < ce:
            # Left to Right
            for i in range(cs, ce):
                spiral.append(matrix[rs][i])
            rs += 1

            # Top to Down
            for i in range(rs, re):
                spiral.append(matrix[i][ce-1])
            ce -= 1

            if not (rs < re and cs < ce):
                break

            # Right to Left
            for i in range(ce-1, cs-1, -1):
                spiral.append(matrix[re-1][i])
            re -= 1

            # Down to Up
            for i in range(re-1, rs-1, -1):
                spiral.append(matrix[i][cs])
            cs += 1

        return spiral

            
