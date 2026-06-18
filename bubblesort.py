def bubble_sort(arr):
    n = len(arr)

    for x in range(n - 1):
        for y in range(n - 1 - x):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]

arr = [4, 88, 27, 61, 18, 9, 81]

print("Unsorted array:", arr)

bubble_sort(arr)

print("Sorted array:", arr)