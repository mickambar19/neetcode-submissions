class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i]== nums[i-1]:
                continue
            j, k = i + 1, len(nums)-1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == 0:
                    triplets.append([nums[i],  nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    while j < k and nums[k] == nums[k-1]:
                        k-=1
                    j += 1
                    k -= 1
                elif current_sum > 0:
                    k-=1
                else:
                    j+= 1
        return triplets