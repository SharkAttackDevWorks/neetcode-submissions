class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        
        
        start = [0,0]

        #create box


        while start[1]< 9: 
            alist = []

            for i in range(start[0], start[0]+3):
                for j in range(start[1], start[1]+3):
                    alist.append(board[i][j])

            start[0]+=3
            if start[0] == 9:
                start[0] = 0
                start[1] += 3

            alist = [x for x in alist if x != "."]
            if len(alist) != len(set(alist)):
                # print("boxes", start)
                # print(alist)
                # print(set(alist))
                return False
        

        for i in range(9):

            alist = board[i]
            alist = [x for x in alist if x != "."]
            if len(alist) != len(set(alist)):
                # print(rows)
                return False




        for j in range(9):
            alist = []
            for i in range(9):
                alist.append(board[i][j])
            
            alist = [x for x in alist if x != "."]
            if len(alist) != len(set(alist)):

                # print(columns)

                return False
            
        return True
