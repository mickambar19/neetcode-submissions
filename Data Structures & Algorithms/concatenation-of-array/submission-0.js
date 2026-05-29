class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        const ans = new Array(nums.length * 2)
        let pos = 0
        for(let i = 0; i < ans.length; i++){
            ans[i] = nums[pos]
            pos++
            if(pos >= nums.length){
                pos = 0
            }
        }
        return ans
    }
}


