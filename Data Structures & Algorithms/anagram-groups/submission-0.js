class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let map = {}

        for (const s of strs){
            const sortedKey = s.split("").sort().join("")
            if(!map[sortedKey]){
                map[sortedKey] =[]
            }
            map[sortedKey].push(s)
        }
       
        return Object.values(map)
    }
}
