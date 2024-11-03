def rotate(my_list, num_rotations):
    window = len(my_list)-num_rotations
    print(window)

    left_str = my_list[:window]
    right_str = my_list[window:]
    print(left_str)
    print(right_str)
    reversed_list = right_str[::-1]
    output = right_str + left_str
    print(output)

rotate(['f', 'e', 'd', 'c', 'a', 'b'],3)

#
# str = "Hello"
# #// 0lleH
# print(str[::-3])