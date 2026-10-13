class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_string = "".join(str(x) for x in digits)
        new_num = int(num_string) + 1
        return [int(x) for x in str(new_num)]
        
        