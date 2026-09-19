class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        col = len(grid[0])
        seen = set()
        res = 0

        def land(x,y):
            adj = []
            if x > 0:
                adj.append((x-1,y))
            if x < rows-1:
                adj.append((x+1,y))
            if y > 0:
                adj.append((x,y-1))
            if y < col-1:
                adj.append((x,y+1))

            # x+1,y x-1,y x,y-1 x,y+1
            
            for node in adj:
                i,ii = node
                val = col*i + ii
                if grid[i][ii] == "1" and val not in seen:
                    seen.add(val)
                    print(i,ii)
                    land(i,ii)    

        for i in range(rows):
            for ii in range(len(grid[i])):
                val = col*i + ii
                if val in seen:
                    continue
                if grid[i][ii] == "1":
                 seen.add(val)
                 land(i,ii)
                 res+=1
                 print("---")

        return res


        