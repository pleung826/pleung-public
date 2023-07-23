class Solution:
    def twoSum(self, nums , target ) :

        comp={}
        for i in range(0, len(nums)):
            if nums[i]==0:
                continue
            if nums[i] in comp:
                comp[nums[i]].append(i)
            else:
                comp[nums[i]] = [i]
        print(comp)

        for i in range(0, len(nums)):
            if nums[i] == 0:
                continue
            diff = target - nums[i]
            if diff in comp:
                if diff == nums[i]:
                    if len(comp[diff]) >=2:
                        return [comp[diff][0], comp[diff][1]]
                else:
                    return [i, comp[diff][0]]

        return []

    def threeSum(self, nums, target):
        for i in range(0,len(nums)):
            nums2=nums.copy()
            nums2[i]=0
            print("target=", target-nums[i], "i=",i, nums2)
            ret=self.twoSum(nums2, target - nums[i])
            if ret != []:
                return [i, ret[0], ret[1]]

        return []


s=Solution()
print(s.twoSum([2,7,11,15], 9))
#print(s.twoSum([3,2,4],4))
#print(s.twoSum([1,2,3,1,2,3],6))
#print(s.threeSum([1,2,3,4,5,6], 13 ))