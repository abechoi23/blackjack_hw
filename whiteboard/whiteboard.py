# Please write a function that sums a list, but ignores any duplicate items in the list.
# For instance, for the list [3, 4, 3, 6] , the function should return 10.



# def sum_nums(a_list):
#     a_dict = {}
#     another_list = a_list[:]
#     for i in a_list:
#         if i in a_dict:
#             a_dict[i] += 1
#         else:
#             a_dict[i] = 1
#         if a_dict[i] > 1:
#             while i in a_list:
#                 another_list.remove(i)
#     print(a_list)
#     return sum(another_list)
    

# a_list = [3, 4, 3, 6, 3, 6]
# print(sum_nums(a_list))


def sum_nums(a_list):
    result = []
    for num in a_list:
        if a_list.count(num) == 1:
            result.append(num)
    return sum(result)

print(sum_nums([3,4,3,6]))


def sumUnique(alist):
    hash_map = {}
    for num in alist:
        if num not in hash_map:
            hash_map[num] = 0
        hash_map[num] += 1
    output = 0
    for k in hash_map:
        if hash_map[k] == 1:
            output+=k
    return output
    # return sum(num for num in hash_map if hash_map[num] == 1)

print(sumUnique([2,3,3,4,1,5,5]))