
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

# given 2 strings, return true if either strings appear at the end of the other
def end_other(a, b):
  a = a.lower()
  b = b.lower()

  # return(b.endswith(a) or a.endswith(b))
  return a[-(len(b)):] == b or a == b[-len(a):]

# given a string, return a string with each char doubled

def double_Char(mystring):
  result = ''
  for char in mystring:
    result += char*2
  return result

# given 3 integer values, return their sum, if numbers are between 13 and 19 they count as 0, except
# for 15 and 16

def no_teen_cum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
  if n [13, 14, 17, 18, 19]:
    return 0
  return n

# return number of even integers in the given array

def count_evens(nums):
  count = 0
  for number in nums:
    if number % 2 == 0:
      count += 1
  return count