# Refactor this code using a stack.

# The program below has a common code smell.
# Here the author is using an array and _manually_
# keeping track of where to add the next item. (Yes, in
# Python you can use a list, but lets assume here that
# `jobs` is only a static array, as it might be in many
# other languages.)

data_stream = ['a', 'p', 'q', 'z', 'g', 'q', 'a', 't', 's', 'l', 'z', 'b', 's']

# next_job_index = 0
# jobs = [None] * 100 # Create an empty 'array'.

# Imagine that data "comes in," one item at a time.
# for data in data_stream:
#     jobs[next_job_index] = data
#     next_job_index += 1

# print(jobs)


# Here, refactor the program using a Stack.
# Hint: This should be simple!
# A Stack class with a `push` operation is provided
# for you.
from simple_stack import Stack

# 1. Instantiate the stack.
s = Stack()

# 2. Iterate over the incoming data stream adding, the data
#    to the stack.
for data in data_stream:
    s.push(data)

# 3. Print the contents of the stack eg. print(foo).
print(s)

