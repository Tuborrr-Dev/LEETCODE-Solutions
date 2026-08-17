class Solution:
    def twoSum(self, number_list: list[int], target: int):
        seen_num = {}
        for index, number in enumerate(number_list):
            other_needed = target - number
            if other_needed in seen_num:
                # then we already have the two numbers we need and return thier indexes
                return [seen_num[other_needed], index]
            # if we havent then we store it in seen with its index
            seen_num[number] = index
        return []
