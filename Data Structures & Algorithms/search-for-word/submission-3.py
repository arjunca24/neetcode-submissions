class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        ans = False
        def find(rem,curr,used):
            nonlocal ans
            if not rem:
                ans = True
                return 
            i,j = curr
            neighbours = []
            if i > 0:
                neighbours.append((i-1,j))
            if i < n-1:
                neighbours.append((i+1,j))
            if j > 0:
                neighbours.append((i,j-1))
            if j < m-1:
                neighbours.append((i,j+1))
            

            for neighbour in neighbours:
                k,l = neighbour
                if board[k][l] == rem[-1] and (k,l) not in used:
                        c = rem.pop()
                        find(rem,(k,l),used + [(k,l)])
                        rem.append(c)
                        
                                


        
        res = list(word)
        res.reverse() 
        for i in range(n):
            for j in range(m):
                if res[-1] == board[i][j]:
                    c = res.pop()
                    find(res,(i,j),[(i,j)])
                    if ans == True:
                        return True
                    res.append(c)
        
        return False




        