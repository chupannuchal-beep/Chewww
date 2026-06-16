def linearSearch(array,search_item):
    for item in range(len(array)):
        if array[item]==search_item:
            return item
    return None
number_array= [1,4,45,90,36,21,43,88,17,16,5]
result=linearSearch(number_array,16)
print("The search item found in index number: ",result)
            