array = [20,35,-15,7,-3,100,55,1,-22]
def BubbleSort(data):
     unsorted = data.copy()
     unsortedPartitionIndex = len(unsorted)
     for j in range(0,unsortedPartitionIndex):
         for i in range(1,unsortedPartitionIndex):
             print('i = ',i)
             if(unsorted[i] == unsorted[i - 1]):
                 return
             if(unsorted[i] < unsorted[i - 1]):
                 unsorted[i],unsorted[i - 1] = unsorted[i - 1],unsorted[i]
                 print('swapped elements')

         unsortedPartitionIndex = unsortedPartitionIndex - 1
     return unsorted

def RecursiveBubble(data):
    unsorted = data.copy()
    unsortedPartitionIndex = len(unsorted)
    def sort(index):
        for i in range(1,index):
            if(unsorted[i] == unsorted[i - 1]):
                return
            if(unsorted[i] < unsorted[i - 1]):
                unsorted[i],unsorted[i - 1] = unsorted[i - 1],unsorted[i]
                print('swapped elements')
        if(index < 1):
            return
        sort(index - 1)
    sort(unsortedPartitionIndex)
    return unsorted
