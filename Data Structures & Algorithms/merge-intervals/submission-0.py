class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        asort = intervals[:]
        asort.sort()


        output = []



        for x in asort:
            if len(output)<1: 
                output.append(x)
                continue
            [startx, endx] =x
            [startl, endl] = output[-1]

            if startx <= endl:
                output[-1] = [startl, endx]

            else:
                output.append(x)




        


        return output


            


