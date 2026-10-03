class Solution:
    def isValid(self, s: str) -> bool:
        


        openstack = []

        if len(s)<2: return False


        for x in s:
            if x in "[{(":
                openstack.append(x)

            else:
                if len(openstack)<1 :
                    return False
                y = openstack.pop(-1)

                if x in "]" and y in "[":
                    continue
                elif x in "}" and y in "{":
                    continue
                elif x in ")" and y in "(":
                    continue
                else:
                    return False

            
        if len(openstack) > 0 :  return False
        return True
