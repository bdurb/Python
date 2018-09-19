
#check if 1, 2, 3 happens in sequence in list
def arrayCheck(nums):
  for i in range(len(nums) - 2):
    if nums[i] == 1 and nums[i + 1]==2 and nums[i + 2]== 3:
      return True
  return False

# return every even index letter from a list
# alternative solution mystring[::2]
def stringBits(mystring):
  result = ''

  for i in range(len(mystring)):
    if i % 2 == 0:
      result = result + mystring[i]

  return result

