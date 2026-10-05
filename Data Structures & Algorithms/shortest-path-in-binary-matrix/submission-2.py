import itertools

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] != 0 : return -1
        if grid[m-1][n-1] != 0 : return -1


        queue = deque()
        queue.append((0,0))

        step = 1

        def bfs(queue):

            nonlocal step

            if grid[m-1][n-1] != 0 : return 

            if len(queue) < 1: return

            _ = (0,1,-1)
            dims = [x for x in itertools.product(_, repeat=2)]
            dims.remove((0,0))

            queue2= deque()


            while len(queue) > 0:

                i, j = queue.popleft()
                grid[i][j] = 2

                for x, y in dims:

                    a = i+x
                    b = j+y

                    if (0<=a<m) and (0<=b<n):
                        print(i, j, a,b)
                        if grid[a][b] == 1: continue
                        if grid[a][b] == 2: continue
                        grid[a][b] = 2
                        queue2.append((a,b))

            
            queue = queue2
            if len(queue)>0:
                step+=1

                bfs(queue)

        bfs(queue)

        print(grid)

        return step
