# def find_sum(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum
#
# print(find_sum(1,2,3,4,5,6,7,8,9))

def print_values(**kwargs):
    for key,values in kwargs.items():
        print(key,values)

print_values(name="John", age="32")