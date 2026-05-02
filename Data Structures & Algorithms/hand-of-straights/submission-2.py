class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = max(hand)
        counter = [0] * (n + 1)
        for val in hand:
            counter[val] += 1

        i = 0
        while i <= n:
            while counter[i] > 0:
                for j in range(groupSize):
                    s = i + j
                    if s > n or counter[s] == 0:
                        return False
                    counter[s] -= 1
            i += 1
        
        return True
        