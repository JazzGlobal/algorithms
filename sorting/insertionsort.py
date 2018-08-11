def InsertionSort(data):
    unsorted = data.copy()
    firstUnsortedIndex = 1
    for j in range(firstUnsortedIndex,len(unsorted)):
        newElement = unsorted[firstUnsortedIndex]
        i = firstUnsortedIndex
        while(i > 0 and unsorted[i - 1] > newElement):
            unsorted[i] = unsorted[i - 1]
            i-=1
        unsorted[i] = newElement
        firstUnsortedIndex+=1
    return unsorted
