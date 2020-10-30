def my_quick_sort(array):
    # if array have 0 or 1 element,return
    if len(array)<2:
        return array
    else:
    # set the first element as pivot
        pivot=array[0]
    # filter out the elements that less than or equal to pivot,then put them into the small list
    # the expression we used in list is called "list comprehension expression"
        smaller = [x for x in array[1:] if x <= pivot]
    # filter out the elements that greater than pivot,then put them into the older list
        older = [x for x in array[1:] if x > pivot]
    # recursive
        return my_quick_sort(smaller)+[pivot]+my_quick_sort(older)

print(my_quick_sort([9,8,7,6,5,4,3,2,1]))