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

def RecursiveInsertion(data):
    unsorted = data.copy()
    firstUnsortedIndex = 1
    def sort(index):
        newElement = unsorted[index]
        i = index
        while(i > 0 and unsorted[i - 1] > newElement):
            print(i)
            unsorted[i] = unsorted[i - 1]
            i -= 1
        unsorted[i] = newElement
        if(index >= len(unsorted) - 1):
            return
        sort(index + 1)
    sort(firstUnsortedIndex)
    return unsorted
