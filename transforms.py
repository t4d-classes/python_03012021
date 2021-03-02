

nums = [1,2,3,4,5]


def double(num):
    return num * 2

def transform(transform_fn, items):

    for item in items:
        print("transform item")
        yield transform_fn(item)
    

# double_nums = []

# for num in nums:
#     double_nums.append(double(num))

double_nums = transform(double, nums)
# double_nums = list(map(double, nums))
# double_nums = list(map(lambda n: n * 2, nums))

for double_num in double_nums:
    print(double_num)
    if double_num > 4: break

# double_nums = [ n * 2 for n in nums ]

print(nums)
print(list(double_nums))