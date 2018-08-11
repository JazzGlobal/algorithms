def SelectionSort(data):
    unsorted = data.copy()
    unsortedPartitionIndex = len(unsorted)
    for j in range(0,unsortedPartitionIndex):
        largest = unsorted[0]
        for i in range(1,unsortedPartitionIndex):
            if(unsorted[i] > largest):
                largest = unsorted[i]
            else:
                i = i + 1
        unsorted[unsorted.index(largest)],unsorted[unsortedPartitionIndex - 1] = unsorted[unsortedPartitionIndex - 1],unsorted[unsorted.index(largest)]
        unsortedPartitionIndex = unsortedPartitionIndex - 1
    return unsorted

def RecursiveSelection(data):
    unsorted = data.copy()
    unsortedPartitionIndex = len(unsorted)

    def sort(index):
        largest = unsorted[0]
        for i in range(1,index):
            if(unsorted[i] > largest):
                largest = unsorted[i]
            else:
                i = i + 1
        unsorted[unsorted.index(largest)],unsorted[index - 1] = unsorted[index - 1],unsorted[unsorted.index(largest)]
        if(index <= 1):
            return
        sort(index - 1)
    sort(unsortedPartitionIndex)
    return unsorted
