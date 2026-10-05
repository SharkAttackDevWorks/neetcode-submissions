class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        graphreq = defaultdict(set)
        graphfoundation = defaultdict(set)

        for x in prerequisites:
            graphreq[x[1]].add(x[0])
            graphfoundation[x[0]].add(x[1])
        

        incomplete = set(x for x in graphreq)
        completed = [x for x in range(numCourses) if x not in incomplete]

        


        old = 0

        print(completed)
        print(incomplete)


        while len(completed) > old:
            old = len(completed)

            for i in range(len(completed)):
                x =completed[i]
                for y in graphfoundation[x]:
                    if y in graphreq and x in graphreq[y]:
                        graphreq[y].remove(x)
                        if len(graphreq[y]) < 1:
                            del graphreq[y]
                            incomplete.remove(y)
                            completed.append(y)
        print(completed)
        print(incomplete)
        if len(incomplete)>0: return False
        return True

        

            
