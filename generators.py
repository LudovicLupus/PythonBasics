# Creating simple python generators

def square_numbers(nums):
    for i in nums:
        yield i*i

my_nums = square_numbers([1,2,3,4,5])

print(my_nums)
# <generator object square_numbers at 0x7f77677d0a98>
# You can iterate over this object as shown below

for num in my_nums:
    print(num)

# Using list comprehensions (note that we are using
# parenthesis around the list comprehension
# This creates a generator objects
my_nums = (x*x for x in [1,2,3,4,5])
print(my_nums)
for num in my_nums:
    print(num)






