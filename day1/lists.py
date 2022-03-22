#to group number strings togethr
nums = [25, 12, 36, 94, 14]
# 0  1  2  3  4
# 25 12 36 95 14
# -5 -4 -3 -2 -1
nums1 = [25, 'str', 12.1]
print(nums1)
# o/p= [25, 'str', 12.1]
#list of list
mil = [nums, nums1]
# o/p=[[25, 12, 36, 94, 14], [25, 'str', 12.1]]
print(mil)
#lists are mutable=valuse can be changed
#append appends in last
nums.append(54)
#insert appends inbetween
nums.insert(2, 77)
print(nums)
#o/p= [25, 12, 77, 36, 94, 14, 54]
# 3delete the number we want to delete as a Value
nums.remove(12)
# to delete at indx number
nums.pop(1)
#to del the multiple valuse
del nums[2:]
#add multiple values
nums.extend([29, 12, 14, 36])
print(nums)
#[25, 36, 29, 12, 14, 36]
#built in functions
min(nums)
max(sum)
sum(nums)
nums.sort()
