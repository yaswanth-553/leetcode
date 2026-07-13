lst = [25,12,8,11,14]
print(lst)
left = 0
right = len(lst)-1
while(left<right):
    lst[left], lst[right] = lst[right], lst[left]
    left += 1
    right -= 1
print(lst)