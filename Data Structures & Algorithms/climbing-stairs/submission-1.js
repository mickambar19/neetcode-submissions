class Solution {

    memCache = {}
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        if (n === 0) return 1

        if (n < 0) return 0
        
        if (this.memCache.hasOwnProperty(n)){
            return this.memCache[n]
        }

        const result = this.climbStairs(n - 2) + this.climbStairs(n - 1)
        this.memCache[n] = result
        return result
    }
}
