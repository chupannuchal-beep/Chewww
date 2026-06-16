def binary_search(array, search_item):
    lowest = 0
    highest = len(array) - 1

    while lowest <= highest:
        mid = (lowest + highest) // 2

        if array[mid] == search_item:
            return mid
        elif array[mid] < search_item:
            lowest = mid + 1
        else:
            highest = mid - 1

    return None


numbers = [2, 5, 7, 10, 15, 20, 25]
result = binary_search(numbers, 10)

if result == None:
    print("Element not found")
else:
    print("The search item found in index number:", result)