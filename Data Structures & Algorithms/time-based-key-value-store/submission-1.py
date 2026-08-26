class TimeMap:

    def __init__(self):
        self.ahash = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ahash:
            self.ahash[key] = [[timestamp, value]]
        else:
            self.ahash[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ahash:
            return -1

        else:
            alist = self.ahash[key]

            if timestamp > alist[-1][0]:
                return alist[-1][1]

            l = 0
            r = len(alist)

            while l <= r:

                c= (l+r)//2

                if alist[c][0] == timestamp:
                    return alist[c][1]

                if alist[c][0] < timestamp:
                    l = c+1

                else:
                    r = c-1

            print(l)
            print(alist)
            return ""