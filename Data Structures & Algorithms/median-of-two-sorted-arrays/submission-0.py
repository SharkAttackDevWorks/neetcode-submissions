class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)

        odd = True

        if (m+n) % 2 == 0:
            odd = False

        h = (m+n) // 2

        if m < n:
            small = nums1
            large = nums2
        
        else:
            small = nums2
            large = nums1


        sn = len(small)
        ln = len(large)

        l = 0
        r = sn

        while l <= sn:

            c = (l+r)//2

            compl = h-c
            print(c, compl)

            if small[c] < large[compl]:
                if odd:
                    return small[c]
                else:
                    if small[c+1] < large[compl]:
                        return (small[c]+small[c+1])/2
                    else:
                        return 
                        return (small[c]+large[compl])/2

            
            else:
                l = c+1

    
