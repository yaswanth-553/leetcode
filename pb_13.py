class palindrome:
    def isPalindrome(self, x):
        if x < 0:
            return "Not a palindrome"
        else:
            original = x
            reverse = 0
            while x > 0:
                rem = x % 10
                reverse = reverse * 10 + rem
                x //= 10
            if original == reverse:
                return "Palindrome"
            else:
                return "Not Palindrome"
