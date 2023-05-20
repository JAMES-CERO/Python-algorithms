# Write your solution for algorithm 3 below

def des_sort_list(lst):
    res  = sorted(lst, reverse = True)
    return res

test3 = des_sort_list([4, 7, 2, 4, 9 ,8])
print(test3)