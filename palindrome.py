class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = str(x)
        reversed_list = x_list[::-1]
        return x_list == reversed_list