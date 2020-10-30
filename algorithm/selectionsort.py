def findsmallest(array):
    min=array[0]
    min_index=0
    for i in range(len(array)):
        if min>array[i]:
            min=array[i]
            min_index=i
    return min_index

def selectionsort(array):
    sortedarray=[]
    i=0
    for i in range(len(array)):
        sortedarray.append(array.pop(findsmallest(array)))
    return  sortedarray




array=[3,4,1,56,-2]
print(selectionsort(array))
