class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(numbers)) :
            hashmap[numbers[i]] = i + 1
        
        for i in range(len(numbers)) :
            val = numbers[i]
            diff = target - val
            if diff == val :
                continue
            if diff in hashmap :
                return [i + 1, hashmap[diff]]
        return [0, len(numbers) - 1]