def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                print(f"Swapping {unsorted_list[j]} and {unsorted_list[j + 1]}")
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
        print(f"List after Pass {i+1}: {unsorted_list}")
        print()  # Print a blank line to separate the passes
    return unsorted_list

unsorted_list = ['D', 'S', 'M', 'R', 'A', 'E']

print("Unsorted List:")
print(unsorted_list)

sorted_list = bubble_sort(unsorted_list)

print("Sorted List:")
print(sorted_list)