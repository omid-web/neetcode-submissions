class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        default_dict = defaultdict(int)
        for num in nums:
            if num in default_dict:
                return True
            default_dict[num] += 1
        return False