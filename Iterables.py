# Practice with iterators and iterables

# Creating simple List object
nums = [x for x in range(3)]

# Lists are iterable because they contain the .__iter__ dunder method
print(dir(nums).__contains__('__iter__'))

# To create an iterator, call .__iter__ on the list
i_nums = nums.__iter__()

# Use built-in functions to handle for dunder method calls
i_nums = iter(nums)

# You can call next() on iterators
# print(dir(i_nums).__contains__('__next__'))
print('__next__' in dir(i_nums))

# <list_iterator object at 0x7ff29c1dd908>
print(i_nums)

# Note that i_nums (the iterator) also contains function .__iter__
# which just returns itself

# Calling next(i_nums) multiple times
print(f'First manual call: {next(i_nums)}')
print(f'Second manual call: {next(i_nums)}')
print(f'Third manual call: {next(i_nums)}')

# Calling next a third time throws a StopIteration exception
# because you've manually hit the end of the iterable list
# print(next(i_nums))

# When iterating over an iterable via a loop, Python knows how to
# handle for these natively. It does something like this:
print('Begin while loop...')
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break












