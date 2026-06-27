x = -121
if x < 0:
    print("Not a palindrome")
else:
    original = x
    reverse = 0
    while x > 0:
        rem = x % 10
        reverse = reverse * 10 + rem
        x //= 10
    if original == reverse:
        print("Palindrome")