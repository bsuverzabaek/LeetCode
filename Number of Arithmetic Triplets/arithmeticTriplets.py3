class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        bag = set()
        count = 0
        for num in nums:
            if num-diff in bag and num-diff*2 in bag:
                count += 1
            bag.add(num)
        return count
