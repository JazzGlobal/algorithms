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
