class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            largest = stones[-1]
            secondlargest = stones[-2]
            if largest == secondlargest:
                stones.pop()
                stones.pop()
            else:
                remainder = largest - secondlargest
                stones.pop()
                stones.pop()
                stones.append(remainder)
                stones.sort()
        
        return stones[0] if stones else 0
