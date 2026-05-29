class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const visitedNums = {}
        for(let idx = 0; idx < nums.length; idx++){
            const num = nums[idx]
            const expectedPair = target-num
            if (visitedNums[expectedPair] !== undefined){
                return [visitedNums[expectedPair], idx]
            }else{
                visitedNums[num] = idx
            }
        }
        return []
    }
}
