def binary_sort(array,item):
    low=0
    high=len(array)-1
    while low<=high:
        mid=int((low+high)/2)
        if array[mid]==item:
            return mid
        elif array[mid]>item:
            high=mid-1
        elif array[mid]<item:
            low=mid+1
        else:
            return None

array=[4,3,2,1]
print(binary_sort(array,3)+1)