class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = []
        right_product = []

        prev_product = 1
        for num in nums:
            temp = prev_product * num
            left_product.append(temp)
            prev_product = temp

        prev_product = 1
        for num in nums[::-1]:
            temp = prev_product * num
            right_product.append(temp)
            prev_product = temp
        right_product = right_product[::-1]

        result = []
        for i in range(len(nums)):
            left = left_product[i-1] if i-1 >= 0 else 1
            right = right_product[i+1] if i+1 < len(nums) else 1
            result.append(left*right)
        
        return result
