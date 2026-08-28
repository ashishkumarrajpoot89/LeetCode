class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        uniquecandy = set(candyType)
        return min(n//2,len(uniquecandy))
        