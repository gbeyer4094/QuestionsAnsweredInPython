def bubble_sort(arr):
    n = len(arr)
    if n > 1:
        for i in range(n - 1):
            # Last i elements are already in place
            for j in range(n - i - 1):
                # Compare adjacent elements
                if arr[j] > arr[j + 1]:
                    # Swap elements
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Example usage
my_list = [5, 3, 8, 2, 1, 4]
print("Original list:", my_list)
bubble_sort(my_list)
print("Sorted list:", my_list)

my_list = [5]
print("Original list:", my_list)
bubble_sort(my_list)
print("Sorted list:", my_list)

my_list = [5, 4]
print("Original list:", my_list)
bubble_sort(my_list)
print("Sorted list:", my_list)
