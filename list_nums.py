from functools import reduce

# mini lab exercise

# update this code to use a function provided by Python which will produce a new list
# of items which pass some conditional expression

# do not use a list comprehension

nums = list(range(10))

# even_nums = []

# for num in nums:
#     if num % 2 == 0:
#         even_nums.append(num)

# even_nums = list(filter(lambda x: x % 2 == 0, nums))
even_nums = [ x for x in nums if x % 2 == 0 ]

print(nums) 
print(even_nums)
print(max(nums))
print(min(nums))
print(sum(nums))

# nums_sum = reduce(lambda acc, cur: acc + cur, nums, 0)

# def sum_two_nums(accumulator, current):
#     print(f"acc: {accumulator}, cur: {current}")
#     return accumulator + current

# nums_sum = reduce(sum_two_nums, nums, 0)

# def double_num(new_list, num):
#     new_list.append(num * 2)
#     return new_list

# double_nums = reduce(double_num, nums, [])

# print(nums)
# print(double_nums)


# for x in range(10, 20, 2):
#     print(x)