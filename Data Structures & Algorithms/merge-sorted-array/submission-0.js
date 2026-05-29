class Solution {
    /**
     * @param {number[]} nums1
     * @param {number} m
     * @param {number[]} nums2
     * @param {number} n
     * @return {void} Do not return anything, modify nums1 in-place instead.
     */
    merge(nums1, m, nums2, n) {
        let left = 0
        let right = 0
        while(left < m){
            if(nums1[left] > nums2[right]){
                let aux = nums1[left]
                nums1[left] = nums2[right]
                nums2[right] = aux
                let j = 0
                while(j < n - 1 && nums2[j] > nums2[j+1]){
                    aux = nums2[j]
                    nums2[j] = nums2[j+1]
                    nums2[j+1] = aux
                    j++
                }
            }
            left++
        }

        while(right < n){
            nums1[right+left] = nums2[right]
            right++
        }
    }
}