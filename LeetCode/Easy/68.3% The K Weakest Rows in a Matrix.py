# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

input1_1 = [[1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1]],
input1_2 = 3

input2_1 = [[1, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0]],
input2_2 = 2


def weakest_rows(mat, k):
    result = []
    strength_list = []

    # get list of strength values
    for row in mat[0]:
        row_strength = 0
        for value in row:
            if value == 1:
                row_strength += 1
        strength_list.append(row_strength)

    # https://www.reddit.com/r/learnpython/comments/gj0nuy/how_to_find_index_of_second_lowest_integer_in/
    for i in range(k):
        # find i from the lowest number, e.g: lowest, second lowest, third lowest, etc.
        value, index = sorted(zip(strength_list, range(len(strength_list))))[i]
        result.append(index)

    return print(result)


weakest_rows(input1_1, input1_2)
weakest_rows(input2_1, input2_2)
