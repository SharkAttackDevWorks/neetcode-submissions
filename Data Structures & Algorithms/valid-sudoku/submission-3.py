class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for arow in board:
            for x in arow:
                if x not in "123456789.":
                    return False
            acount = Counter(arow)
            for x in acount:
                if acount[x]>1 and x!= ".":
                    return False
        board2 = list(row for row in zip(*board))

        for arow in board2:
            for x in arow:
                if x not in "123456789.":
                    return False
            acount = Counter(arow)
            for x in acount:
                if acount[x]>1 and x!= ".":
                    return False

        x = defaultdict(list)
        for i in range(9):
            for j in range(9):
                x[(i//3,j//3)].append(board[i][j])
        print(len(x))
        alist = [x[key] for key in x]
        print(alist)
        for arow in alist:
            for x in arow:
                if x not in "123456789.":
                    print(arow, x)
                    return False
            acount = Counter(arow)
            for x in acount:
                if acount[x]>1 and x!= ".":
                    print(arow, x)
                    return False

        return True
        
        
                
        

            