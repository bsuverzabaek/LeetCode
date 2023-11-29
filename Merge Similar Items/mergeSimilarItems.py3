class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        index = Counter(dict(items1))
        index += Counter(dict(items2))
        return sorted(index.items())
