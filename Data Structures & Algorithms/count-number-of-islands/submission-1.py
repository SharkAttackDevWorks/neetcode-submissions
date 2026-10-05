class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        curr = 1
        

        def flood(i, j, grid, curr):

            def recursive(i, j, grid, curr):

                if  (0<=i<len(grid) and (0<=j<len(grid[0]))) and grid[i][j] == "1":
                        grid[i][j] = str(curr)
                        recursive(i+1, j, grid, curr)
                        recursive(i-1, j, grid, curr)
                        recursive(i, j+1, grid, curr)
                        recursive(i, j-1, grid, curr)
                
            recursive(i, j, grid, curr)

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1":
                    curr+=1
                    flood(i, j, grid, curr)

        

        output = []

        for x in grid:
            for y in x:
                output.append(int(y))


        amax =  max(output)

        

        if amax >1:
            return amax-1

        if amax == 1:
            return amax

        return 0

        
        


                
