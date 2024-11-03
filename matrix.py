def maxMatrixSum(matrix):
    i=0
    max_digit = []
    max_index = []
    while (i<len(matrix)):
        print("Iteration",i)
        max_elm = max(matrix[i])
        idx= (matrix[i].index(max_elm))
        if idx not in max_index:
            max_digit.append(max_elm)
            max_index.append(idx)
        else:
            #Check for the next lesser value with different index
            matrix[i].remove(max_elm)
            max_elm = max(matrix[i])
            idx = (matrix[i].index(max_elm))
            max_digit.append(max_elm)
            max_index.append(idx)



        # print(max_elm)
        # print(idx)
        #
        print("digit=", max_digit)
        print("idx = ", max_index)
        print("sum =", sum(max_digit))
        i = i+1


    return (sum(max_digit))


matrix = [[-5,2,3,4],[6,7,8,9],[10,-1,12,13],[14,15,-4,16]]

print(maxMatrixSum(matrix))