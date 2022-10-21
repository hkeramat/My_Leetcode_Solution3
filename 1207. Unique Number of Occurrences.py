class Solution:
    import collections
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = set()
        for item in (collections.Counter(arr).values()):
            if item in occurrences:
                return False
            occurrences.add(item)
        return True
