#duplication
arr = [1,4,4,4,2,3]
n = len(arr)
count =0


class Algorithm:
    def twoPointer(self,nums:List[int])->int:
        # largest and second largest number
        largest = float("-inf")
        = float("-inf")
            
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
    def hasLargestSecondLargest(self,nums: List[int])->int:
        n = len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j+1]>nums[j]:
                    nums[j],nums[j+1]= nums[j+1],nums[j]
        return(nums[n-1],nums[n-2])

    # def removeDuplicates(self,nums: List[int])->int:
