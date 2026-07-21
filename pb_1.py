#two sum problem solution with better time complexity and space complexity
nums = [3,3]
target = 6
hashmap = {}
for i in range(len(nums)):
    complement = target - nums[i]
    if complement in hashmap:
        print(hashmap[complement], i)
        break
    hashmap[nums[i]] = i
    