class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0]
        # [22,21,20]
        # [22,21,20] i = 1 j = 2
        # [22,21,20] i = 1 j = 2

        for i in range(len(temperatures)-2, -1, -1):
            currentTemp = temperatures[i]
            passedDays = 0
            for j in range(i+1, len(temperatures)): 
                if currentTemp < temperatures[j]:
                    passedDays = j-i
                    break
            results.append(passedDays)
        return results[::-1]
            
        