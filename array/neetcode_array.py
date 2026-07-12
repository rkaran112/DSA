#duplication
arr = [1,4,4,4,2,3]
n = len(arr)
count =0


class Algorithm:
    def twoPointer(self,nums:list[int])->int:
        # largest and second largest number
        largest = float("-inf")
        second  = float("-inf")
            
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False


    def hasLargestSecondLargest(self,nums: list[int])->int:
        n = len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j+1]>nums[j]:
                    nums[j],nums[j+1]= nums[j+1],nums[j]
        return(nums[0],nums[1])

    # def removeDuplicates(self,nums: List[int])->int:
    def largestSecondLargest2(self,nums:list[int])->int:
        largest = float("-inf")
        second  = float("-inf")
        for num in nums:
            # 5 7 10 10
            if num>largest:
                second = largest
                largest = num
            elif num >second and largest>num:
                second = num
        return largest, second

    def arrayRotaion(self,nums:list[int])->list[int]:
        n = len(nums)
        first = nums[n-1]
        for i in range(n-1):
            nums[i] = nums[i+1] 
        nums[0] = first
        return nums

    def largestElement(self,nums):
        largest = nums[0]
        n = len(nums)
        for i in range(1,n):
            if nums[i]>largest:
                largest = nums[i]
        return largest
sol = Solution()
print(sol.largestElement([3,5,7,1,2]))
# print(sol.arrayRotaion([3,4,5,1,2]))