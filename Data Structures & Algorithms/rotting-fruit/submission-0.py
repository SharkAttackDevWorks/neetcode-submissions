class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rottens = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottens.append((i,j)) 
                if grid[i][j] == 1:
                    fresh+=1

        step = 0

        def bfs(rottens, grid):

            nonlocal step, fresh

            if fresh < 1:
                return

            rottens2 = deque()

            while len(rottens)>0:

                

                i, j = rottens.popleft()

                dims = [(0,1), (1,0), (0,-1), (-1,0)]

                for x, y in dims:
                    a = i+x
                    b = j+y
                    if (0<=a<len(grid)) and (0<=b<len(grid[0])):
                        if grid[a][b] == 1:
                            grid[a][b] = 2
                            rottens2.append((a,b))
                            fresh-=1

            if len(rottens2) > 0:
                step+=1
                rottens = rottens2
                bfs(rottens, grid)


        bfs(rottens, grid)

        if step > 0: return step
        return -1


                
                