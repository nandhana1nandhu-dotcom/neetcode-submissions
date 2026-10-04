class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
         for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    if j-i<=k:
                       return True
         return False