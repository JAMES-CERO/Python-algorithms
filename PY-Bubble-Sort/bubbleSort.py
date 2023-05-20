# write your bubble sort algorithm below

# def bubble_sort(lst):
#     for i in range(len(lst) -1):
#         print(f"iteration ")
#         for j in range(len(lst) -1):
#             print(f"comparing {lst[j], lst[j+1]}")
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     print(lst)

#///////////////// We can improve this algorithm so that when the list is passed through without making any swaps, the algorithm will stop. This is because the list is sorted when it is passed through without any swaps.


def bubble_sort(lst):
    for i in range(len(lst) -1):
        swapped = False
        print(f"iteration ")
        for j in range(len(lst) -1):
            print(f"comparing {lst[j], lst[j+1]}")
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            return
    print(lst)


    
bubble_sort([1, 4, 2, 8, 3])
sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")


