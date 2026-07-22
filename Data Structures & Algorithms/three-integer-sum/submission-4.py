class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        for i in range(len(nums)):
            target = -nums[i]
            j = i + 1
            k = len(nums)-1
            if i > 0 and nums[i]== nums[i-1]:
                continue
            while j < k:
                if j == i:
                    j+=1
                    continue
                if k == i:
                    k-=1
                    continue
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == 0:
                    triplets.append([nums[i],  nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    while j < k and nums[k] == nums[k-1]:
                        k-=1
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    j+= 1
        return triplets