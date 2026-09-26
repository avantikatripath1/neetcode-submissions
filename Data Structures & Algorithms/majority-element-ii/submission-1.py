class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        output = []
        counts = Counter(nums)
        for num, counter in counts.items():
            if counter > (len(nums)//3):
                output.append(num)
        return output